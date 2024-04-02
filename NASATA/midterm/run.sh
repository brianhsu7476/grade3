#!/bin/bash
cd test
for i in {1..10}; do
	mkdir a
	ln -s a b
	cd a
done
echo > c
