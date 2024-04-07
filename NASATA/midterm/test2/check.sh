#!/usr/bin/env bash

script=$1

run(){
	if [[ $3 == 'l' ]]; then
		timeout 60s ./$script -l $1 > output/$2.txt
	else
		timeout 60s ./$script $1 > output/$2.txt
	fi
	if [[ $? -eq 124 ]]; then
		echo -e "$2: \033[0;33mTime Limit Exceeded\[033[0m"
	elif [[ -z `diff sample_output/$2.txt output/$2.txt` ]]; then
		echo -e "$2: \033[0;32mAccept\033[0m"
	else
		echo -e "$2: \033[0;31mWrong Answer\033[0m"
	fi
}

run exponential 1-1 n
run shortestpath 1-2 n
run loop1 1-3 n
run loop2 1-4 n
run t3 1-5 n
run big 2-1 n
run t1 2-2 n
run t2 2-3 n
run exponential 3-1 l
run shortestpath 3-2 l
run loop1 3-3 l
run loop2 3-4 l
run t3 3-5 l
run big 4-1 l
run t1 4-2 l
run t2 4-3 l

