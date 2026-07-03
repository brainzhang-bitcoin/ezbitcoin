```
require 'securerandom'
require 'digest'
require 'openssl'

# -------------------
# 1. Generate Entropy
# -------------------
bytes = SecureRandom.random_bytes(16) # 16 bytes = 128 bits
entropy = bytes.unpack("B*").join
puts "entropy: #{entropy}"

# ----------------------
# 2. Entropy to Mnemonic
# ----------------------
# 1. Create checksum
size = entropy.length / 32 # number of bits to take from hash of entropy (1 bit checksum for every 32 bits entropy)
sha256 = Digest::SHA256.digest([entropy].pack("B*")) # hash of entropy (in raw binary)
checksum = sha256.unpack("B*").join[0..size-1] # get desired number of bits
puts "checksum: #{checksum}"

# 2. Combine
full = entropy + checksum
puts "combined: #{full}"

# 3. Split in to strings of 11 bits
pieces = full.scan(/.{11}/)

# 4. Get the wordlist as an array
wordlist = File.readlines("wordlist.txt")

# 5. Convert groups of bits to array of words
puts "words:"
sentence = []
pieces.each do |piece|
  i = piece.to_i(2)   # convert string of 11 bits to an integer
  word = wordlist[i]  # get the corresponding word from wordlist
  sentence << word.chomp # add to sentence (removing newline from end of word)
  puts "#{piece} #{i.to_s.rjust(4)} #{word}"
end

mnemonic = sentence.join(" ")
puts "mnemonic: #{mnemonic}"

# -------------------
# 3. Mnemonic to Seed
# -------------------
passphrase = "" # can leave this blank
puts "passphrase: #{passphrase}"

password = mnemonic
salt = "mnemonic#{passphrase}" # "mnemonic" is always used in the salt with optional passphrase appended to it
iterations = 2048
keylength = 64
digest = OpenSSL::Digest::SHA512.new

result = OpenSSL::PKCS5.pbkdf2_hmac(password, salt, iterations, keylength, digest) # password, salt, iter, keylen, digest
seed = result.unpack("H*")[0] # convert to hexadecimal string
puts "seed: #{seed}"
```