#!/bin/bash

VIS=()
all=()
n=0

vis(){
	for i in ${VIS[@]}; do
		if [[ $1 == $i ]]; then echo '1'; exit 0; fi
	done
	echo '0'
}

dfs(){
	local cur=`pwd`; local a=`ls`
	VIS+=($cur)
	all+=($cur)
	for i in $a; do
		if [[ -f $i ]]; then all+=("$cur/$i"); continue; fi
		local j=$i;
		if [[ -L $i ]]; then j=`readlink $i`; fi
		cd $j; j=`pwd`; cd $cur
		if [[ `vis $j` == '0' ]]; then cd $j; dfs; cd $cur; fi
	done
}

dfs2(){
	local cur=`pwd`
}

if [[ $# != 1 ]]; then echo 'error'; exit 1; fi

cd $1
dfs
n=${#all[@]}
