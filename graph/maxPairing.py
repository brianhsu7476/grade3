from random import *

a=input().split(' ')
b=input().split(' ')
assert(len(a)==6)
assert(len(b)==6)
a=[float(i) for i in a]
b=[float(i) for i in b]
for i in a:
	assert(i>=0)
for i in b:
	assert(i>=0)
sa=sum(a)
sb=sum(b)
a=[i/sa for i in a]
b=[i/sb for i in b]
print(a)
print(b)
mxid=[]
mx=0
for i in range(64):
	j=[i>>k&1 for k in range(6)]
	if sum(j)!=3:
		continue
	sc=sum([b[k] if j[k] else a[k] for k in range(6)])
	if sc==mx:
		mxid.append(i)
	elif sc>mx:
		mxid=[i]
		mx=sc
for i in mxid:
	print([i>>k&1 for k in range(6)])

