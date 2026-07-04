# How to Close Lightning Channels by Lnd-cli?

越来越有老年痴呆的倾向，这个命令至少Google过3次了，每次都忘，被自己蠢哭了~~

|  |  |
| --- | --- |
| ``` 1 ``` | ``` lncli closechannel <fund_txid> [fund_tx_vout_NO] ``` |

不要忘了vout\_NO，不然会报错”channel not found”