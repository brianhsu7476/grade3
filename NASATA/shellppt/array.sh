#!/usr/bin/env bash
echo "$0 $1 $2"
echo $(($1+$2))
echo "$# $@"
arr=(`ls`)
echo ${arr[0]}
IFS=' '
arr=(`ls`)
echo ${arr[0]}
