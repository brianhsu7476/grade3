def myStrategy(pastPriceVec, currentPrice):
	import numpy as np
	import pandas as pd
	data=pastPriceVec+[currentPrice]
	try:
		par=pd.read_csv('myPar2.csv')
		n, ob, os=int(par['n']), float(par['overbought']), float(par['oversold'])
	except:
		n, ob, os=14, 0.8, 0.2
	smau, smad=0, 0
	for i in range(min(n, len(data)-1)):
		d=data[-i-1]-data[-i-2]
		if d>0:
			smau+=d
		if d<0:
			smad-=d
	rsi=smau/(smau+smad)
	if rsi<os:
		return 1
	if rsi>ob:
		return -1
	return 0

