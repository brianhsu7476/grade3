#!/usr/bin/env bash

for i in {1..4}; do
	f="a$i"
	if [[ -d $f ]]; then rm -r $f; fi
	if [[ -e $f ]]; then rm $f; fi
	mkdir $f; cd $f
	j="a$(((i+0)%4+1))"
	k="a$(((i+1)%4+1))"
	l="a$(((i+2)%4+1))"
	m="a$(((i+3)%4+1))"
	n="a$(((i+4)%4+1))"
	echo 'hi' > $f
	ln -s ../$j/$f $k
	ln -s ../$m $n
	mkdir $l; cd $l
	echo 'hi' > $f
	ln -s ../../$m $n
	cd ../..
done
