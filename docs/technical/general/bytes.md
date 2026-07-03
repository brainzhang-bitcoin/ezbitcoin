```
# Work with bytes directly using hexadecimal characters to represent each byte.
bytes = "\xF9\xBE\xB4\xD9" #=> (jargon - tries to display character encoding for each byte value)

# Bytes -> Hexadecimal String
hex_string = bytes.unpack("H*")[0] #=> "f9beb4d9"

# Hexadecimal String -> Bytes
bytes = [hex_string].pack("H*") #=> (jargon - tries to display a character encoding for each byte value)

# Hexadecimal String -> Integer
integer = hex_string.to_i(16) #=> 4190024921
```

Ruby can be a bit awkward when displaying bytes. If you try to print out bytes directly, Ruby will try to display them using each byte's character encoding (instead of their hexadecimal representation), so you need to convert to hexadecimal to display them when debugging.

The "pack" and "unpack" functions are the most useful when it comes to working with raw bytes of data in languages like Ruby and Python, so it's worth getting to know them.