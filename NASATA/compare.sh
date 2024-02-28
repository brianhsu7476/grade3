#!/usr/bin/env bash

arga=''
argl=''
argn='.*'
argr=''
cnt=0

error(){
	echo 'usage: ./compare.sh [OPTION] <PATH A> <PATH B>'
	echo 'options:'
	echo '-a: compare hidden files instead of ignoring them'
	echo '-h: output information about compare.sh'
	echo '-l: treat symlinks as files instead of ignoring them'
	echo '-n <NAME>: compare only files whose paths contain <NAME> as a substring'
	echo '-r: compare directories recursively'
	exit 1
}

isfile(){
	if [[ -L $1 ]]; then
		if [[ $argl ]]; then echo 1; else echo 0; fi
	elif [[ -f $1 ]]; then echo 1
	else echo 0
	fi
}

isdir(){
	if [[ -L $1 ]] || ! [[ -d $1 ]]; then echo 0; else echo 1; fi
}

df(){
	if [[ -L $1 ]]; then
		if [[ -L $2 ]]; then
			if [[ `readlink $1` == `readlink $2` ]]; then echo ''; exit 0
			else echo '100'; exit 0; fi
		else echo '100'; exit 0; fi
	elif [[ -L $2 ]]; then echo '100'; exit 0; fi
	local a=`diff -d $1 $2`
	if [[ $a == '' ]]; then echo ''; exit 0; fi
	if [[ `cut -c 1-3 <<< $a`  == 'Bin' ]]; then echo '100'; exit 0; fi
	local ca=0; local cb=0
	while IFS= read -r line; do
		local b=`cut -c 1 <<< $line`
		if [[ $b == '<' ]]; then (( ca++ )); fi
		if [[ $b == '>' ]]; then (( cb++ )); fi
	done <<< $a
	local c=$((`wc -l < $1`-ca))
	if [[ $ca -lt $cb ]]; then ca=$cb; fi
	echo $((100*ca/(c+ca)))
}

dfs(){
	local a='ls'
	if [[ $arga == 1 ]]; then a='ls -a'; fi
	for i in `$a`; do
		if [[ $i == '.' ]] || [[ $i == '..' ]]; then continue
		elif [[ `isdir $i` == 1 ]]; then
			echo "$1$i/"; cd $i
			dfs "$1$i/"
			cd ..
		else echo "$1$i"; fi
	done
}

while getopts "ahln:r?" argc; do
	case $argc in
		a)
			arga=1; cnt=$((cnt+1))
			;;
		h)
			error
			;;
		l)
			argl=1; cnt=$((cnt+1))
			;;
		n)
			argn=$OPTARG; cnt=$((cnt+2))
			;;
		r)
			argr=1; cnt=$((cnt+1))
			;;
		?)
			error
			;;
	esac
done

cnt=$((cnt+1))
da=${!cnt}
cnt=$((cnt+1))
db=${!cnt}

if ! [[ $argr ]]; then
	if [[ `isfile $da` == 0 ]] || [[ `isfile $db` == 0 ]]; then error; fi
	a=`df $da $db`
	if [[ $a != '' ]]; then echo "changed $a%"; fi
	exit 0
elif [[ `isdir $da` == 0 ]] || [[ `isdir $db` == 0 ]]; then error
fi

d0=`pwd`; A=();
if [[ $da != '' ]]; then cd $da; fi
a=`dfs ''`
for i in $a; do A+=($i); done
cd $d0
if [[ $db != '' ]]; then cd $db; fi
a=`dfs ''`
for i in $a; do A+=($i); done
cd $d0
IFS=$'\n'; B=`LC_ALL=C sort <<< ${A[*]}`; unset IFS
A=()
for i in $B; do A+=($i); done
B=()
for ((i=0; i<${#A[@]}; i++)); do
	if [[ $i == 0 || ${A[$i]} != ${A[$(($i-1))]} ]]; then B+=(${A[$i]}); fi
done

for i in ${B[@]}; do
	if ! [[ $i =~ $argn ]]; then continue; fi
	if [[ `isfile $da/$i` == 1 ]]; then
		if [[ `isfile $db/$i` == 1 ]]; then
			a=`df $da/$i $db/$i`
			if [[ $a != '' ]]; then echo "$i: changed $a%"; fi
		else echo "delete $i"; fi
	elif [[ `isfile $db/$i` == 1 ]]; then echo "create $i"; fi
done
