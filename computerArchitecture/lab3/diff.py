import sys

a, b=[], []
for line in open(sys.argv[1]):
	a.append(line)
for line in open(sys.argv[2]):
	b.append(line)
cnt=0
for i in range(len(a)):
	if(a[i]!=b[i]):
		print('line', i+1)
		print('\033[31m<', a[i], end='')
		print('\033[32m>', b[i], '\033[0m', end='')
		cnt+=1
	if(cnt==5):
		break

