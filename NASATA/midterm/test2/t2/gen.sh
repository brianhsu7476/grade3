#!/usr/bin/env bash

for i in {1..7}; do
	mkdir b$i; cd b$i
	a=b$(((i*6)%7+1))
	ln -s ../$a/$a link$i
	echo 'hi' > hi
	for j in {1..7}; do
		mkdir b$j; cd b$j
		b=b$(((i*2+j*6)%7+1))
		ln -s ../../$b/$a/$b link$j
		echo 'hello' > hello
		for k in {1..7}; do
			mkdir b$k; cd b$k
			c=b$(((i*3+j*2+k*6)%7+1))
			ln -s ../../../$c/$b/$a link$k
			echo 'world' > world
			cd ..
		done
		cd ..
	done
	cd ..
done
