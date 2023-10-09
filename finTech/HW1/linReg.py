import sys
from numpy import *
import pandas as pd

csvName, ws='0050.TW.csv', 10 # ws=windowSize
trainDate=['2019-01-01', '2023-01-01']
valDate=['2023-01-01', '2099-01-01']

dat=pd.read_csv(csvName).to_numpy()
# 0:Date 1:Open 2:High 3:Low 4:Close 5:Adj Close 6:Volume

tdat, vdat=[], []
for i in range(len(dat)):
	if trainDate[0]<=dat[i][0] and dat[i][0]<trainDate[1]:
		tdat.append(dat[i][5])
	if valDate[0]<=dat[i][0] and dat[i][0]<valDate[1]:
		vdat.append(dat[i][5])
tdat, vdat=array(tdat), array(vdat)

def phi(dat):
	return [1]+[(dat[i+1]-dat[i])/dat[i] for i in range(len(dat)-1)]

def rrv(w, vdat):
	c0=1000
	c=c0
	s=0
	for i in range(len(vdat)):
		if i<ws-1: continue
		x=phi(vdat[i-ws+1:i+1])
		if dot(w, x)>0 and s==0:
			s=c/vdat[i]
			c-=s*vdat[i]
		elif dot(w, x)<0 and s>0:
			c+=s*vdat[i]
			s=0
	return (s*vdat[-1]+c)/c0

X=array([phi(tdat[i:i+ws]) for i in range(len(tdat)-ws)])
y=array([(tdat[i]-tdat[i-1])/tdat[i-1] for i in range(ws, len(tdat))])
w=dot(linalg.pinv(X), y)
print(w)
print(rrv(w, vdat))
