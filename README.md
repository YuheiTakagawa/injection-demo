# demo 2018/04/11

This repository use ELF(testpy) which made from my private repository.  

## Server side usage
Server side show data(output of client) from socket which made by injection code.
```
# Setting IP Address(Hard code), run server
cd server
gcc -o server server.c
setup.sh

# From other terminal, sending command to client with netcat. Destination IP isHard code.
send.sh '<command>'
# For example, target command is python.
# send.sh 'python'
```


## Client side usage
Client size show data.

```
# Setting IP Address(Hard code), run injection daemon.
cd client
setup.sh

# From other terminal, running command
# For example, target command is python show images.
showimages.py <IMAGE PATH>
```


