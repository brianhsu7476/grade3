#!/usr/bin/env bash
min(){
	local res=$1
	for i in $@; do
		if [[ $i -lt $res ]]; then
			res=$i
		fi
	done
	echo $res
}
echo `min 3 1 4 1 5 9`
