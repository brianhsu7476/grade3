import numpy as np
from scipy.stats import *

def err9(tml):
	#tml=22/3*np.log(2)
	pfa=1-gamma.cdf(tml*9, 9, loc=0, scale=3)
	pmiss=gamma.cdf(tml*9, 9, loc=0, scale=6)
	#print(0.8*pfa+0.2*pmiss)
	return 0.8*pfa+0.2*pmiss
def err1(tml):
	#tml=18*np.log(2)
	pfa=1-expon.cdf(tml, loc=0, scale=3)
	pmiss=expon.cdf(tml, loc=0, scale=6)
	#print(0.8*pfa+0.2*pmiss)
	return 0.8*pfa+0.2*pmiss

print(min(list(range(10000)), key=lambda x:err9(x/100))/100)
print(min(list(range(10000)), key=lambda x:err1(x/100))/100)
