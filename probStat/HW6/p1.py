import numpy as np
import matplotlib.pyplot as plt

def draw(mu0, mu1):
	t=[i/100 for i in range(10000)]
	x=[np.exp(-mu0*i) for i in t]
	y=[1-np.exp(-mu1*i) for i in t]
	plt.plot(x, y)
	plt.xlabel('$P_{FA}$')
	plt.ylabel('$P_{MISS}$')
	plt.title('ROC for $\mu_O='+str(mu1)+'$')
	plt.savefig('muO'+str(mu1)+'.png')
	plt.close()

draw(3, 6)
draw(3, 10)
