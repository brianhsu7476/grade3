#!/usr/bin/env bash

# Task 1
./script.sh exponential > output/1-1.txt
./script.sh shortestpath > output/1-2.txt
./script.sh loop1 > output/1-3.txt
./script.sh loop2 > output/1-4.txt
./script.sh t3 > output/1-5.txt

# Task 2
./script.sh big > output/2-1.txt
./script.sh t1 > output/2-2.txt
./script.sh t2 > output/2-3.txt

# Task 3
./script.sh -l exponential > output/3-1.txt
./script.sh -l shortestpath > output/3-2.txt
./script.sh -l loop1 > output/3-3.txt
./script.sh -l loop2 > output/3-4.txt
./script.sh -l t3 > output/3-5.txt

# Task 4
./script.sh -l big > output/4-1.txt
./script.sh -l t1 > output/4-2.txt
./script.sh -l t2 > output/4-3.txt
