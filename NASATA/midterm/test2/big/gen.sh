#!/usr/bin/env bash

for i in {1..490}; do
	mkdir a
	ln -s a/a b
	cd a
done
mkdir a
echo > c
