#!/bin/sh
ifconfig em0 192.168.11.1
ip=`ifconfig em0 | awk '/inet / {print $2}'`
echo "IP Address:" $ip
pid=`ps ax | grep injd | grep -v $0 | grep -v grep| sed 's/^ *//g' | cut -d' ' -f1`
if [ -n "$pid" ]; then
	kill $pid
fi
/CR_for_FreeBSD/testpy/injd &
echo "Finished setup, Please run target program in other terminal."
