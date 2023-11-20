#!/bin/bash
if [[ $# -ne 1 ]]; then exit 1; fi
if ! [[ -d out ]]; then mkdir out; fi
cp code/src/*.v out/
cp code/supplied/*.v out/
cp testcases/instruction_$1.txt out/instruction.txt
cp testcases/output_$1.txt out/
cd out
iverilog -o CPU.out *.v
./CPU.out > /dev/null
diff output.txt output_$1.txt
echo finish
