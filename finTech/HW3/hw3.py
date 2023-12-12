from hashlib import *
import math
from random import *
from numpy import *

p=2**256-2**32-2**9-2**8-2**7-2**6-2**4-1
a=0
b=7
g=[0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8]
zero=[2**512, 2**512]
n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
num=2085

def inv(c):
	return pow(c, p-2, p)

def add(c, d):
	if c==zero:
		return d
	if d==zero:
		return c
	if c[0]==d[0] and c[1]!=d[1]:
		return zero
	s=(3*c[0]**2+a)*inv(2*c[1])%p if c==d else (d[1]-c[1])*inv(d[0]-c[0])%p
	x3=(s**2-c[0]-d[0])%p
	return [x3, (s*(c[0]-x3)-c[1])%p]

def mul(c, d):
	r=zero
	while d:
		if d&1:
			r=add(r, c)
		c=add(c, c)
		d>>=1
	return r

def sgn(sk, m): # sign
	e=sha256(m).hexdigest()
	z=int(e, 16)
	k=randint(1, n-1)
	h=mul(g, k)
	r=h[0]
	s=pow(k, -1, n)*(z+r*num)%n
	return mul(g, sk), r, s

def ver(pk, r, s, m): # verify
	e=sha256(m).hexdigest()
	z=int(e, 16)
	w=pow(s, -1, n)
	u1, u2=z*w%n, r*w%n
	h=add(mul(g, u1), mul(pk, u2))
	return h[0]==r

print(mul(g, 4))
print(mul(g, 5))
print(mul(g, num))
print(bin(num))
m=b'Hello World!'
pk, r, s=sgn(num, m)
print(r, s)
print(ver(pk, r, s, m))

# Problem 8 below
A=[[1, 1, 1], [4, 2, 1], [9, 3, 1]]
b=[10, 20, num]
x=dot(linalg.inv(A), b)
p=10007
a=[round(i*2)*pow(2, -1, p)%p for i in x]
print(a)

def P(x):
	return (a[0]*x**2+a[1]*x+a[2])%p

print(P(1), P(2), P(3))
