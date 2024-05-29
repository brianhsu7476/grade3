#!/bin/bash
a=`ps aux | grep ' ping'`
IFS=$'\n'
mode='safe'
if [[ $1 == 'kill' ]]; then
	mode='unsafe'
fi
for i in $a; do
	id=`echo "$i" | cut -c 12-16`
	if [[ $mode == 'safe' ]]; then echo $i
	else kill -9 $id; fi
done
unset IFS
