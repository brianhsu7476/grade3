# 7.3343526679107836 [ 0.00823331 -0.04023871  0.08947945 -0.05024477  0.12391539  0.00555206 -0.00444235]

def myStrategy(pastPriceVec, currentPrice):
	import numpy as np
	import pandas as pd
	data=pastPriceVec+[currentPrice]
	nmaShort, nmaLong=8, 13
	nRSI=20
	nKD, r=9, 2/3
	w=[0.00823331, -0.04023871, 0.08947945, -0.05024477, 0.12391539, 0.00555206, -0.00444235]
	try:
		par=pd.read_csv('myPar4.csv')
		a, b=float(par['a'])/10, float(par['b'])/10
	except:
		a, b=0, -0.1

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

	X=[]
	for i in range(len(data)):
		maShort=np.mean(data[max(i+1-nmaShort, 0):i+1])
		maLong=np.mean(data[max(i+1-nmaLong, 0):i+1])
		smau, smad=0, 0
		for j in range(min(nRSI, i)):
			dd=data[i-j]-data[i-j-1]
			if dd>0:
				smau+=dd
			if dd<0:
				smad-=dd
		rsi=(0 if smau+smad==0 else smau/(smau+smad))
		X.append([1, data[i], maShort, maLong, rsi, k[i], d[i]])
		#y.append(data[i+1]-data[i])
	X=np.array(X)
	#y=np.array(y)
	if np.dot(w, X[-1])>a:
		return 1
	if np.dot(w, X[-1])<b:
		return -1
	return 0
