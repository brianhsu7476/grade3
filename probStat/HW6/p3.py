import numpy as np
from scipy.stats import *

tml=22/3*np.log(2)
pfa=1-gamma.cdf(tml*9, 9, loc=0, scale=3)
pmiss=gamma.cdf(tml*9, 9, loc=0, scale=6)
print(0.8*pfa+0.2*pmiss)
tml=18*np.log(2)
pfa=1-expon.cdf(tml, loc=0, scale=3)
pmiss=expon.cdf(tml, loc=0, scale=6)
print(0.8*pfa+0.2*pmiss)
