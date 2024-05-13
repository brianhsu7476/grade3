from random import *

def f():
	t=0
	s=0
	while True:
		u=0
		if random()<0.4:
			u+=1
		if random()<0.6:
			u+=1
		if u==2:
			s+=3
		if u==1:
			s+=1
		t+=1
		if s>3:
			return -1
		if s==3:
			return t

a=[]
for i in range(1000000):
	res=f()
	if res!=-1:
		a.append(res)
print(sum(a)/len(a))

