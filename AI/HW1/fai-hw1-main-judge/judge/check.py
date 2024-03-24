import subprocess
import os
import pandas as pd

subprocess.run('cp example_search.py ./search.py', shell=True)
subprocess.run('python3 judge.py', shell=True)
subprocess.run('cp output.csv example_output.csv', shell=True)
subprocess.run('cp ../../hw1-code/search.py ./', shell=True)
subprocess.run('python3 judge.py', shell=True)

a=pd.read_csv('example_output.csv').to_dict()
b=pd.read_csv('output.csv').to_dict()
n=len(a['Path Length'])
for i in range(n):
	print(a['Path Length'][i], b['Path Length'][i])
for i in range(n):
	print('-', end='')
print()
for i in range(n):
	print(a['States Explored'][i], b['States Explored'][i])

