#!/bin/bash
for a in {-3..3}; do
	for b in {-3..3}; do
		echo 'a,b' > myPar4.csv
		echo "$a,$b" >> myPar4.csv
		echo "$a,$b"
		python3 rrEstimate.py myStrategy.py 2> /dev/null
	done
done
