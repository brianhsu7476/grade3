def myStrategy(pastPriceVec, currentPrice):
	import numpy as np
	import pandas as pd
	data=pastPriceVec+[currentPrice]
	try:
		par=pd.read_csv('myPar3.csv')
		n, r=int(par['n']), float(par['r'])
	except:
		n, r=9, 2/3
	rsv=[]
	k, d=[], []
	for i in range(len(data)):
		mnn, mxn=data[i], data[i]
		for j in range(max(i+1-n, 0), i+1):
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
	#print(k)
	#print(d)
	if k[-1]>d[-1]:
		return 1
	if k[-1]<d[-1]:
		return -1
	return 0

