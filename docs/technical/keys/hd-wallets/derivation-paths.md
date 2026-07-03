This code requires the [bitcoin-ruby](https://github.com/lian/bitcoin-ruby) library.

```
require 'bitcoin' # sum gem install bitcoin-ruby

seed = "67f93560761e20617de26e0cb84f7234aaf373ed2e66295c3d7397e6d7ebe882ea396d5d293808b0defd7edd2babd4c091ad942e6a9351e6d075a29d4df872af"

# ------
# BIP 44
# ------
# Note: Hardened keys start at 2**31 (the second half of the 2**32 possible children).

m = Bitcoin::ExtKey.generate_master(seed.htb) # convert hex to binary
purpose   = m.derive(2**31+44) # m/44'
coin_type = m.derive(2**31+44).derive(2**31+0) # m/44'/0'
account   = m.derive(2**31+44).derive(2**31+0).derive(2**31+0) # m/44'/0'/0'
receiving = m.derive(2**31+44).derive(2**31+0).derive(2**31+0).derive(0) # m/44'/0'/0'/0

20.times do |i| 
	puts receiving.derive(i).addr # m/44'/0'/0'/0/*
end
```