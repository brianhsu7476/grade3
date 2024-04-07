#!/usr/bin/env bash

# Task 1
./script.sh exponential > output/exponential.txt
./script.sh shortestpath > output/shortestpath.txt
./script.sh loop1 > output/loop1.txt
./script.sh loop2 > output/loop2.txt

# Task 2
./script.sh big > output/big.txt

# Task 3
./script.sh -l exponential > output/exponential-2.txt
./script.sh -l shortestpath > output/shortestpath-2.txt
./script.sh -l loop1 > output/loop1-2.txt
./script.sh -l loop2 > output/loop2-2.txt

# Task 4
./script.sh -l big > output/big-2.txt
