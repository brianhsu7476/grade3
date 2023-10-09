import sys
from numpy import *
import pandas as pd

csvName='0050.TW.csv'
trainDate=['2019-01-01', '2023-01-01']
valDate=['2023-01-01', '2099-01-01']

dat=pd.read_csv(csvName)
head=dat.columns.values
dat=dat.to_numpy()
# 0:Date 1:Open 2:High 3:Low 4:Close 5:Adj Close 6:Volume

tdat, vdat=[], []
for i in range(len(dat)):
	if trainDate[0]<=dat[i][0] and dat[i][0]<trainDate[1]:
		tdat.append(dat[i])
	if valDate[0]<=dat[i][0] and dat[i][0]<valDate[1]:
		vdat.append(dat[i])

tdat=pd.DataFrame(tdat, columns=head)
tdat.to_csv('train.csv', index=False)
vdat=pd.DataFrame(vdat, columns=head)
vdat.to_csv('val.csv', index=False)

