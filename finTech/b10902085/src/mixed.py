import sys
from numpy import *
import pandas as pd

calVal=False
nmaShort, nmaLong=8, 13
nRSI=20
nKD, r=9, 2/3
nfold=20

t=pd.read_csv('train.csv')['Adj Close'].values
v=pd.read_csv('val.csv')['Adj Close'].values
data=list(t)+list(v)

rsv=[]
k, d=[], []
for i in range(len(data)):
	mnn, mxn=data[i], data[i]
	for j in range(max(i+1-nKD, 0), i+1):
		mnn=min(mnn, data[j])
		mxn=max(mxn, data[j])
	if mxn==mnn:
		rsv.append(100)
	else:
		rsv.append((data[i]-mnn)/(mxn-mnn)*100)
for i in range(len(data)):
	if i==0:
		k.append(rsv[i])
		d.append(rsv[i])
	else:
		k.append(r*k[-1]+(1-r)*rsv[i])
		d.append(r*d[-1]+(1-r)*k[i])

X, y=[], []
for i in range(len(data)-1):
	maShort=mean(data[max(i+1-nmaShort, 0):i+1])
	maLong=mean(data[max(i+1-nmaLong, 0):i+1])
	smau, smad=0, 0
	for j in range(min(nRSI, i)):
		dd=data[i-j]-data[i-j-1]
		if dd>0:
			smau+=dd
		if dd<0:
			smad-=dd
	rsi=(0 if smau+smad==0 else smau/(smau+smad))
	X.append([1, data[i], maShort, maLong, rsi, k[i], d[i]])
	y.append(data[i+1]-data[i])
X=array(X)
y=array(y)

Xt, yt, Xv, yv=[], [], [], []

if calVal:
	Xv, yv=X[len(t):], y[len(t):]
	X, y=X[:len(t)], y[:len(t)]

idx=random.permutation(len(X))
mnw, mnerr=[], 1e9
for i in range(nfold):
	Xt, yt=[], []
	if not calVal:
		Xv, yv=[], []
	for j in range(len(X)):
		if len(X)*i//nfold<=j and j<len(X)*(i+1)//nfold:
			if not calVal:
				Xv.append(X[idx[j]])
				yv.append(y[idx[j]])
		else:
			Xt.append(X[idx[j]])
			yt.append(y[idx[j]])
	w=dot(linalg.pinv(Xt), yt)
	err=linalg.norm(yv-dot(Xv, w))
	if err<mnerr:
		mnerr=err
		mnw=w

print(mnerr, mnw)
