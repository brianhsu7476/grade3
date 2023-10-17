#!/bin/bash
for n in {5..20}; do
	for rr in {1..9}; do
		echo 'n,r' > myPar3.csv
		echo "$n,0.$rr" >> myPar3.csv
		echo "$n,0.$rr"
		python3 rrEstimate.py myStrategy3.py 2> /dev/null
	done
done
