#!/bin/bash
cd code
g++ helloworld.cpp
./a.out
cd ..
cp code/output2.txt hello.txt
if [[ -d .code.backup ]]; then rm -r .code.backup; fi
cp -r code .code.backup
if [[ -L link1 ]]; then rm link1; fi
if [[ -L link2 ]]; then rm link2; fi
if [[ -L link3 ]]; then rm link3; fi
ln -s code/helloworld.cpp link1
ln -s .code.backup link2
ln -s link2 link3
