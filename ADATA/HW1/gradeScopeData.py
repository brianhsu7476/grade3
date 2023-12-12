import sys
from math import *
from numpy import *
from random import *
import pandas as pd
import matplotlib.pyplot as plt

#mxsc=[4, 4, 3, 3, 2, 4, 5, 5, 4, 5, 5, 4, 7]
#maxScore=sum(mxsc)
e=0.7

def avg(x):
	return sum(x)/len(x)
def var(x):
	return sum([i**2 for i in x])/len(x)-avg(x)**2
def sig(x):
	return sqrt(var(x))
def cov(x, y):
	assert(len(x)==len(y))
	r=0
	for i in range(len(x)):
		r+=x[i]*y[i]
	r/=len(x)
	r-=avg(x)*avg(y)
	return r
def cor(x, y):
	return cov(x, y)/sqrt(var(x)*var(y))
def draw(x, y, s):
	#plt.plot(x, y, label='o')
	plt.plot(x, y, linestyle='None', marker='o', markersize='2', label=s)
	#plt.show()

assert(len(sys.argv)==2)
data=pd.read_csv(sys.argv[1])
data.drop(data.loc[data['Status']=='Missing'].index, inplace=True)
n=len(data)
prob, mxsc=[], []
for i in data.columns:
	if i[0].isnumeric():
		prob.append(i)
		for j in range(len(i)-3):
			if i[j:j+3]=='pts':
				for k in range(j, -1, -1):
					if i[k]=='(':
						mxsc.append(float(i[k+1:].split(' ')[0]))
						break
				break
print(mxsc)
maxScore=int(sum(mxsc))
data.insert(0, 'Sum', [sum([data[j].values[i] for j in prob]) for i in range(n)], False)
data=data.sort_values(by='Sum', ascending=False)
#print(data)
res=array([[cor(data[i].values, data[j].values) for j in prob] for i in prob])
print(res)
#x=[sum([data[prob[j]].values[i] for j in range(-5, -2)])+random()*0.4-0.2 for i in range(n)]
#y=[sum([data[prob[j]].values[i] for j in range(-2, 0)])+random()*0.4-0.2 for i in range(n)]
xx=[i/10 for i in range(maxScore*10+1)]
icnt=0
for i in prob:
	y=data[i].values
	x=[data['Sum'].values[j]-y[j] for j in range(n)]
	yy=[]
	for j in xx:
		qq=sum([e**abs(j-k) for k in data['Sum'].values])
		yy.append(sum([data[i].values[k]*e**abs(j-data['Sum'].values[k])/qq for k in range(n)]))
	yy=[j/mxsc[icnt] for j in yy]
	draw(xx, yy, i+str(round(cor(x, y), 3)))
	icnt+=1
leg = plt.legend(loc='best')
plt.show()
