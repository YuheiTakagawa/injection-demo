#!/bin/sh

if [ $# -ne 1 ]; then
	echo "Usage: sendcm '<target>'"
fi
echo $1 | nc -u -w0 192.168.11.1 8090
