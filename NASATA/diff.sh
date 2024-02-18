#!/bin/bash
error(){ echo 'Wrong!'; exit 1; }

if [[ $# != 2 ]]; then error; fi

a=`diff $1 $2`;
if [[ $a == '' ]]; then echo '0'; exit 0; fi
if [[ `cut -c 1-3 <<< $a`  == 'Bin' ]]; then echo '100'; exit 0; fi
ca=0; cb=0;
while IFS= read -r line; do
	b=`cut -c 1 <<< $line`;
	if [[ $b == '<' ]]; then (( ca++ )); fi
	if [[ $b == '>' ]]; then (( cb++ )); fi
done <<< $a
c=$((`wc -l < $1`-ca));
if [[ $ca -lt $cb ]]; then ca=$cb; fi
echo $((100*ca/(c+ca)));
