#!/bin/bash
for n in {10..20}; do
	for ob in {1..9}; do
		for os in {1..9}; do
			if [[ $ob -ge $os ]]; then
				echo 'n,overbought,oversold' > myPar2.csv
				echo "$n,0.$ob,0.$os" >> myPar2.csv
				echo "$n,0.$ob,0.$os"
				python3 rrEstimate.py myStrategy2.py 2> /dev/null
			fi
		done
	done
done
