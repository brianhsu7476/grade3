#!/usr/bin/env bash

cmd='gcc -std=c99 -O2'
$cmd $1 -o gen
$cmd $2 -o sol
$cmd $3 -o main
for ((i=1; i<=$4; ++i)); do
	./gen $i > 'in.txt'
	./sol < 'in.txt' > sol.txt
	./main < 'in.txt' > main.txt
	if [[ `diff sol.txt main.txt` ]]; then
		echo -e "Test $i:"
		echo -e "Input:"
		echo '--------------------'
		cat 'in.txt'
		echo '--------------------'
		echo -e "Output of $2:"
		echo '--------------------'
		cat sol.txt
		echo '--------------------'
		echo -e "Output of $3:"
		echo '--------------------'
		cat main.txt
		echo '--------------------'
		break
	fi
done
rm gen
rm sol
rm main
rm 'in.txt'
rm sol.txt
rm main.txt
