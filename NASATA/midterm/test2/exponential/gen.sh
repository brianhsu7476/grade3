#!/usr/bin/env bash

for i in {1..10}; do
	mkdir b
	ln -s b a
	cd b
done
echo > c
