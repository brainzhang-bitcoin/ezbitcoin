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

Ruby 在显示字节时可能有点别扭。如果您尝试直接打印出字节，Ruby 将尝试使用每个字节的字符编码来显示它们（而不是它们的十六进制表示），因此在调试时您需要将它们转换为十六进制以便显示。

在诸如 Ruby 和 Python 等语言中处理原始数据字节时，“pack” 和 “unpack” 函数是最有用的，因此很值得去了解和熟悉它们。