#!/bin/bash

if [[ -z $1 ]]; then
	echo 'error'
	exit 1
fi

tmp='tmp1048576'

pin(){
	ping 192.168.1.1 > $tmp/$1
}

if ! [[ -d $tmp ]]; then
	mkdir $tmp
fi
for ((i=0; i<$1; ++i)); do
	echo $i
	pin $i &
done
