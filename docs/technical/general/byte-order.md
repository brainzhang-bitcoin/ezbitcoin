```
![Copy](../../images/icons_clipboard-white.svg)



![Copied](../../images/icons_clipboard-check-white.svg)copied



![Failed](../../images/icons_clipboard-x-white.svg)copied

# hexadecimal string
hex_string = "6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000"

# reverse byte order in hexadecimal string
hex_string_reversed = hex_string.scan(/../).reverse.join
puts hex_string_reversed #=> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
# TIP: scan(/../) matches every two characters in a string and returns an array


# raw bytes
bytes = "\x6F\xE2\x8C\x0A\xB6\xF1\xB3\x72\xC1\xA6\xA2\x46\xAE\x63\xF7\x4F\x93\x1E\x83\x65\xE1\x5A\x08\x9C\x68\xD6\x19\x00\x00\x00\x00\x00"

# reverse raw bytes
bytes_reversed = bytes.reverse
puts bytes_reversed.unpack("H*")[0] #=> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```