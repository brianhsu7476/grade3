#!/usr/bin/env bash

export LC_ALL=C
cur=`pwd`; lc=$((${#cur}+1))

cutl(){ echo "$1" | rev | cut -d '/' -f 1 --complement | rev; }
cutol(){ echo "$1" | rev | cut -d '/' -f 1 | rev; }
cutf(){ echo "$1" | cut -c 1-$lc --complement; }

argl=0
while getopts "l" argc; do
	case $argc in
		l)
			argl=1; shift
			;;
	esac
done

a=`find "$1" | sort`
declare -A G; declare -A vis; declare -A stk
for i in $a; do G[$i]=''; vis[$i]=0; stk[$i]=0; done

dfs(){
	tt=1
	if [[ ${stk[$1]} == 1 ]]; then return 1; fi
	if [[ ${vis[$1]} == 1 ]]; then return 0; fi
	vis[$1]=1; stk[$1]=1
	local tmp; local i; local j
	IFS=';' read -r -a tmp <<< "${G[$1]}"; unset IFS
	for i in ${tmp[@]}; do
		j=`echo "$i" | cut -d ',' -f 2`; dfs $j
		if [[ $? == 1 ]]; then return 1; fi
	done
	stk[$1]=0
	return 0
}

for i in $a; do
	if [[ -d $i ]]; then for j in `ls $i`; do
		if [[ -L $i/$j ]]; then
			cd $i; k=`readlink $j`
			cd `cutl $k`; l=`cutf "$(pwd)/$(cutol $k)"`
			G[$i]+="$j,$l"; cd $cur
		else G[$i]+="$j,$i/$j;"; fi
	done fi
done

if [[ $argl == 1 ]]; then
	declare -A ans; bfs=($1); i=0
	ans[$1]=$1; vis[$1]=1
	while [[ $i -lt ${#bfs[@]} ]]; do
		x=${bfs[$i]}; i=$((++i))
		IFS=';' read -r -a tmp <<< "${G[$x]}"; unset IFS
		for j in ${tmp[@]}; do
			k=`echo $j | cut -d ',' -f 1`; l=`echo $j | cut -d ',' -f 2`
			if [[ ${vis[$l]} == 0 ]]; then
				ans[$l]="${ans[$x]}/$k"
				bfs+=($l); vis[$l]=1
			fi
		done
	done
	for i in $a; do if [[ ${ans[$i]} ]]; then echo "${ans[$i]} -> $i"; fi done
else
	dfs $1
	if [[ $? == 1 ]]; then echo 'loops detected'
	else echo 'no loops detected'; fi
fi
