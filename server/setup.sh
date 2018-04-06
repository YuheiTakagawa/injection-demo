#!/bin/sh

ifconfig enp0s25 192.168.11.2
ip=`ifconfig enp0s25 | awk '/inet/ {print $1}' | awk -F: '{print $2'} | head -n1`
echo "IP Address:" $ip

echo "RUN server program"
echo "/demo/send.sh '<target>"
./server
