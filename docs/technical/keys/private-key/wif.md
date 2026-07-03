```
# ---------
# Functions
# ---------

require 'digest'

# hash256 function (checksums use hash256)
def hash256(hex)
  binary = [hex].pack("H*")
  hash1 = Digest::SHA256.digest(binary)
  hash2 = Digest::SHA256.digest(hash1)
  result = hash2.unpack("H*")[0]
  return result
end

# checksum function
def checksum(hex)
  hash = hash256(hex) # Hash the data through SHA256 twice
  return hash[0...8]  # Return the first 4 bytes (8 characters)
end

# base58 encode function
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

# ----------
# WIF Encode
# ----------

# 1. start with a 32-byte hexadecimal private key
privatekey = "ef235aacf90d9f4aadd8c92e4b2562e1d9eb97f0df9ba3b508258739cb013db2" # example, do not use

# 2. add prefix (80 = mainet, ef = testnet)
data = "80" + privatekey

# 3. add compression byte (optional)
data = data + "01"

# 4. add checksum
data = data + checksum(data)

# 5. base58 encode
wif = base58_encode(data)

# result
puts wif #=> L5EZftvrYaSudiozVRzTqLcHLNDoVn7H5HSfM9BAN6tMJX8oTWz6
```