# How to Set Systemd Startup Script for Bitcoind?

## setup bitcoind.service

|  |  |
| --- | --- |
| ``` 1 ``` | ``` vim /etc/systemd/system/bitcoind.service ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` [Unit] Description=Bitcoin daemon After=network.target  [Service] ExecStart=/opt/node/bitcoin/bin/bitcoind -daemon -conf=/opt/node/bitcoin/blockdata/bitcoin.conf -pid=/run/bitcoind/bitcoind.pid # Creates /run/bitcoind owned by bitcoin RuntimeDirectory=bitcoind RuntimeDirectoryPreserve=yes User=ubuntu Type=forking PIDFile=/run/bitcoind/bitcoind.pid Restart=on-failure StandardOutput=/var/log/bitcoind.log StandardError=/var/log/bitcoind.log  # Hardening measures ####################  # Provide a private /tmp and /var/tmp. PrivateTmp=true  # Mount /usr, /boot/ and /etc read-only for the process. ProtectSystem=full  # Disallow the process and all of its children to gain # new privileges through execve(). NoNewPrivileges=true  # Use a new /dev namespace only populated with API pseudo devices # such as /dev/null, /dev/zero and /dev/random. PrivateDevices=true  [Install] WantedBy=multi-user.target ``` |

## Reload systemctl daemon

|  |  |
| --- | --- |
| ``` 1 ``` | ``` systemctl daemon-reload ``` |

## Enabled new bitcoind service

|  |  |
| --- | --- |
| ``` 1 ``` | ``` systemctl enable bitcoind ``` |

## Commands to start or stop the service

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` systemctl stop bitcoind systemctl start bitcoind ``` |

## Show service status

|  |  |
| --- | --- |
| ``` 1 ``` | ``` systemctl status bitcoind.service ``` |

More info in:

https://github.com/bitcoin/bitcoin/tree/master/contrib/init