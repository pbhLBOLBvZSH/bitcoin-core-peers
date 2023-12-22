Simple script to connect to as many peers as you can.

Uses: https://bitnodes.io/api/v1/snapshots/latest/

Add the following to to your bitcoin core config file:
```
maxconnections=999999

[main]
rpcuser=username
rpcpassword=password
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcport=8332
```
And update the username and password at line 24 in main.py.

