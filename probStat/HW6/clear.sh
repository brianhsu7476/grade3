#!/bin/bash

echo 'This will erase all 1.tex to 100.tex. Enter y to continue...'
read a
if [[ $a != 'y' ]]; then
	echo 'No file will be removed.'
	exit 0
fi

for i in {1..100}; do
	if [[ -f $i.tex ]]; then
		echo '\begin{pr}' > $i.tex
		echo '' >> $i.tex
		echo '\end{pr}' >> $i.tex
	fi
done
