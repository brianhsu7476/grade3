#!/usr/bin/env bash

for i in {1..100}; do
	f="a$i"
	if [[ -d $f ]]; then rm -r $f; fi
	if [[ -e $f ]]; then rm $f; fi
	mkdir $f; cd $f
	j="a$(((i+36)%100+1))"
	k="a$(((i+52)%100+1))"
	l="a$(((i+72)%100+1))"
	m="a$(((i+60)%100+1))"
	n="a$(((i+58)%100+1))"
	echo 'hi' > $f
	ln -s ../$j/$f $k
	ln -s ../$m $n
	mkdir $l; cd $l
	echo 'hi' > $f
	ln -s ../../$m $n
	cd ../..
done
