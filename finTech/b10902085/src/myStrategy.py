def myStrategy(pastPriceVec, currentPrice):
	import numpy as np
	import pandas as pd
	data=pastPriceVec+[currentPrice]
	try:
		assert(0)
		par=pd.read_csv('myPar1.csv')
		nmaShort, nmaLong=int(par['nmaShort']), int(par['nmaLong'])
		alpha, beta=float(par['alpha']), float(par['beta'])
	except:
		nmaShort, nmaLong=8, 13
		alpha, beta=-1, 0
	#print(nmaShort, nmaLong, alpha, beta)
	maShort=np.mean(data[max(-nmaShort, -len(data)):])
	maLong=np.mean(data[max(-nmaLong, -len(data)):])
	if maShort>maLong+alpha:
		return 1
	if maShort<maLong-beta:
		return -1
	return 0

