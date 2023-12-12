from math import *
import matplotlib.pyplot as plt
def avg(x):
	return sum(x)/len(x)
def var(x):
	return sum([i**2 for i in x])/len(x)-avg(x)**2
def var1(x):
	a=avg(x)
	return sum([(i-a)**2 for i in x])/(len(x)-1)
def sig(x):
	return sqrt(var(x))
def sig1(x):
	return sqrt(var1(x))
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
def linComb(x, y, w): # w, 1-w
	w2=1-w
	mu=w*avg(x)+w2*avg(y)
	vr=w**2*var(x)+w2**2*var(y)+2*w*w2*cov(x, y)
	return mu, vr
def draw(x, y):
	plt.plot(x, y, label="line")
	plt.show()
def frontier(x, y):
	z=[linComb(x, y, i/100) for i in range(101)]
	xx=[sqrt(i[1]) for i in z]
	yy=[i[0] for i in z]
	draw(xx, yy)

x=[1, 2, 3, 4, 5]
y=[10, 8, 6, 4, 2]
frontier(x, y)
