```
![Copy](../../../images/icons_clipboard-white.svg)



![Copied](../../../images/icons_clipboard-check-white.svg)copied



![Failed](../../../images/icons_clipboard-x-white.svg)copied

require 'openssl' # HMAC
require 'ecdsa'   # sudo gem install ecdsa

# ----
# Seed
# ----
seed = "67f93560761e20617de26e0cb84f7234aaf373ed2e66295c3d7397e6d7ebe882ea396d5d293808b0defd7edd2babd4c091ad942e6a9351e6d075a29d4df872af"
puts "seed: #{seed}"
puts

# --------------------
# Generate Master Keys
# --------------------
# seed
# |
# m

# HMAC
hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA512.new, "Bitcoin seed", [seed].pack("H*")) # digest, key, data
master_private_key = hmac[0..63] # left side of digest
master_chain_code = hmac[64..-1] # right side of digest

# > The SHA512-HMAC function is reused because it is already part of the standard elsewhere, but it takes a key in addition to the data being hashed.
# As the key can be arbitrary, we opted to use to make sure the key derivation was Bitcoin-specific. -- Pieter Wuille

# Get Public Key (multiply generator point by private key)
master_public_key = ECDSA::Group::Secp256k1.generator.multiply_by_scalar(master_private_key.to_i(16)) # multiply generator point by private key
master_public_key = ECDSA::Format::PointOctetString.encode(master_public_key, compression: true).unpack("H*")[0] # encode to compressed public key format

puts "master_chain_code:  #{master_chain_code}"  #=> 463223aac10fb13f291a1bc76bc26003d98da661cb76df61e750c139826dea8b
puts "master_private_key: #{master_private_key}" #=> f79bb0d317b310b261a55a8ab393b4c8a1aba6fa4d08aef379caba502d5d67f9
puts "master_public_key:  #{master_public_key}"  #=> 0252c616d91a2488c1fd1f0f172e98f7d1f6e51f8f389b2f8d632a8b490d5f6da9
puts

# --------------------------
# Child Extended Private Key
# --------------------------
# m
# |- m/0
# |- m/1
# |- m/2
# .
# .
# .
# |- m/2147483648 (hardened - m/0')
parent_private_key = master_private_key
parent_chain_code  = master_chain_code
i = 0 # child number

# Normal (parent public key can create child public key for this private key)
if i < 2**31
    point = ECDSA::Group::Secp256k1.generator.multiply_by_scalar(parent_private_key.to_i(16)) # multiply generator point by private key
    point = ECDSA::Format::PointOctetString.encode(point, compression: true).unpack("H*")[0] # encode to compressed public key format
    data = [point].pack("H*") + [i].pack("N")     # point(private_key) i
end

# > This means that it is possible to give someone a parent extended key (public key + chain code), and they can derive all public keys in the chain. -- Pieter Wuille

# Hardened (parent public key cannot create public key for this private key)
if i >= 2**31
  data = ["00"].pack("H*") + [parent_private_key].pack("H*") + [i].pack("N")  # 0x00 private_key i
end

# > Hardened derivation should be the default unless there is a good reason why you need to be able to generate public keys without access to the private key. -- Pieter Wuille
# > You cannot derive hardened public keys from xpubs, because hardening is specifically designed to make exactly that impossible. -- Pieter Wuille

# Put data and key through hmac
key = [parent_chain_code].pack("H*") # chain code is key for hmac
hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA512.new, key, data) # digest, key, data
il = hmac[0..63]  # left side of intermediate key [32 bytes]
ir = hmac[64..-1] # right side of intermediate key [32 bytes]

# Chain code is last 32 bytes
child_chain_code = ir

if child_chain_code.to_i(16) >= ECDSA::Group::Secp256k1.order
    raise "Chain code is greater than the order of the curve. Try the next index."
end

# Work out the corresponding public key too (optional)
child_private_key = (il.to_i(16) + parent_private_key.to_i(16)) % ECDSA::Group::Secp256k1.order # (il + parent_key) % n
child_private_key = child_private_key.to_s(16).rjust(64, '0') # convert to hex (and make sure it's 32 bytes long)

if child_private_key.to_i(16) == 0
    raise "Child private key is zero. Try the next index."
end

child_public_key = ECDSA::Group::Secp256k1.generator.multiply_by_scalar(child_private_key.to_i(16)) # work out the public key for this too
child_public_key = ECDSA::Format::PointOctetString.encode(child_public_key, compression: true).unpack("H*")[0] # encode to compressed public key format

puts "child_chain_code:   #{child_chain_code}"
puts "child_private_key:  #{child_private_key}"
puts "child_public_key:   #{child_public_key}"
puts

# -------------------------
# Child Extended Public Key
# -------------------------
# m -------- p
#            |- p/0
#            |- p/1
#            |- p/3
parent_public_key = master_public_key
parent_chain_code = master_chain_code
i = 0 # child number

if i >= 2**31
    raise "Can't create hardened child public keys from parent public keys."
end

key = [parent_chain_code].pack("H*")
data = [parent_public_key].pack("H*") + [i].pack("N") # 32-bit unsigned, network (big-endian) byte order

# Put data and key through hmac
hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA512.new, key, data)
il = hmac[0..63]  # left side of intermediate key [32 bytes]
ir = hmac[64..-1] # right side of intermediate key [32 bytes]

# Chain code is last 32 bytes
child_chain_code = hmac[64..-1]

if il.to_i(16) >= ECDSA::Group::Secp256k1.order
    raise "Result of digest is greater than the order of the curve. Try the next index."
end

# Work out the child public key
point_hmac   = ECDSA::Group::Secp256k1.generator.multiply_by_scalar(il.to_i(16))                               # convert hmac il to a point
point_public = ECDSA::Format::PointOctetString.decode([parent_public_key].pack("H*"), ECDSA::Group::Secp256k1) # convert parent_public_key to a point
point = point_hmac.add_to_point(point_public)                                                                  # point addition

if (point == ECDSA::Group::Secp256k1.infinity)
    raise "Child public key point is at point of infinity. Try the next index."
end

child_public_key = ECDSA::Format::PointOctetString.encode(point, compression: true).unpack("H*")[0] # encode to compress public key

puts "child_chain_code:   #{child_chain_code}"
puts "child_public_key:   #{child_public_key}"
puts

# --------------------------
# Extended Key Serialization
# --------------------------

# Utils - Needed for creating the fingerprint and checksum, and converting hex string to Base58
# -----
require 'digest'

def create_fingerprint(parent_public_key)
    hash160 = Digest::RMD160.digest(Digest::SHA256.digest([parent_public_key].pack("H*"))) # hash160 it
    fingerprint = hash160[0...4].unpack("H*").join # take first 4 bytes (and convert to hex)
    return fingerprint
end

def hash256(hex)
    binary = [hex].pack("H*")
    hash1 = Digest::SHA256.digest(binary)
    hash2 = Digest::SHA256.digest(hash1)
    result = hash2.unpack("H*")[0]
    return result
end

def checksum(hex)
    hash = hash256(hex) # Hash the data through SHA256 twice
    return hash[0...8]  # Return the first 4 bytes (8 characters)
end

def base58_encode(hex)
    chars = %w[
      1 2 3 4 5 6 7 8 9
    A B C D E F G H   J K L M N   P Q R S T U V W X Y Z
    a b c d e f g h i j k   m n o p q r s t u v w x y z
    ]
    base = chars.length

    i = hex.to_i(16)
    buffer = String.new

    while i > 0
        remainder = i % base
        i = i / base
        buffer = chars[remainder] + buffer
    end

    # add '1's to the start based on number of leading bytes of zeros
    leading_zero_bytes = (hex.match(/^([0]+)/) ? $1 : '').size / 2

    ("1"*leading_zero_bytes) + buffer
end

# ---------
# Serialize
# ---------
parent_public_key = master_public_key # needed to create fingerprint

chain_code  = child_chain_code # m/0
private_key = child_private_key # m/0

# version + depth + fingerprint + childnumber + chain_code + key + (checksum)
#
# version:     puts xprv or xpub at the start
# depth:       how many times this child has been derived from master key (0 = master key)
# fingerprint: created from parent public key (allows you to spot adjacent xprv and xpubs)
# childnumber: the index of this child key from the parent
# chain_code:  the current chain code being used for this key
# key:         the private or public key you want to create a serialized extended key for (prepend 0x00 for private)

version     = "0488ade4" # private = 0x0488ade4 (xprv), public = 0x0488b21e (xpub)
depth       = "01"
fingerprint = create_fingerprint(parent_public_key) #=> "018c1259"
childnumber = "00000000" # 4 byte hexadecimal string
chain_code  = chain_code
key         = "00" + private_key  # prepend 00 to private keys (to make them 33 bytes, the same as public keys)

serialized = version + depth + fingerprint + childnumber + chain_code + key
extended_private_key = base58_encode(serialized + checksum(serialized))

puts "extended_private_key: #{extended_private_key}"
```