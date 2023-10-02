#!/bin/bash

if [ ! -n "$1" ]; then
  echo "Usage: judge.sh <Asm File>"
  exit 0
fi
File=${1:-"hw1.s"}
TmpDir=$(mktemp -d)
AC="/tmp2/b10902083/ac"
function JudgeDone() {
  if [[ -n "$1" ]]; then
    echo "Something goes wrong on Input:"
    echo "Verdict: $1"
    cat "$TmpDir/01.in"
    echo "Correct Answer is:"
    cat "$TmpDir/01.ans"
    echo "User output is:"
    cat "$TmpDir/01.out"
  fi
  echo "Congrats! for 0 <= A, B < 10, and 0 <= operator <= 6, your program output the same as the judge"
  if [[ ! $(basename $File) =~ ^b[0-9]{8}\.s$ ]]; then
    echo "Just remember to check your filename before you submit"
    echo "Should be b1XXXXXXX.s"
  fi
  rm -rf $TmpDir
  exit 0
}

function judge() {
  i=$1
  op=$2
  j=$3
  if ((i==0 && op==5 && j==0)); then
    return;
  fi
  TmpACOut=$(mktemp)
  TmpUserOut=$(mktemp)
  #printf "$i\n$op\n$j\n"
  printf "$i\n$op\n$j\n" | $AC > $TmpACOut
  printf "$i\n$op\n$j\n" | jupiter $File > $TmpUserOut
  if ! diff -q $TmpACOut $TmpUserOut; then
    printf "$i\n$op\n$j\n" > 01.in
    cp $TmpACOut $TmpDir/01.ans
    cp $TmpUserOut $TmpDir/01.out
    rm $TmpACOut $TmpUserOut
    JudgeDone "Wrong Answer"
  fi
  rm $TmpACOut $TmpUserOut
}

UP=9
N=20
(
cnt=0
for i in $(seq 0 $UP); do
  for op in $(seq 0 6); do
    for j in $(seq 0 $UP); do
    ((cnt=cnt%N)); ((cnt++==0)) && wait && echo "Running on: $i $op $j"
       judge $i $op $j &
    done
  done
done
)

JudgeDone
