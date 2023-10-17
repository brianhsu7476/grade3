#!/bin/bash
for s in {1..10}; do
	for l in {11..20}; do
		for a in {-3..3}; do
			for b in {-3..3}; do
				echo 'nmaShort,nmaLong,alpha,beta' > myPar1.csv
				echo "$s,$l,$a,$b" >> myPar1.csv
				echo "$s,$l,$a,$b"
				python3 rrEstimate.py myStrategy1.py 2> /dev/null
			done
		done
	done
done
