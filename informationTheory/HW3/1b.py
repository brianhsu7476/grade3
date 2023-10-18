import matplotlib.pyplot as plt

def addPoint(x, y, label):
	if label=='none':
		label='$('+str(x)+', '+str(y)+')$'
	plt.annotate('  '+label, xy=(x, y))

p0, p1=0.2, 0.3
pt=[]
for i in range(10000):
	pt.append([1-(1-p0)**i, (1-p1)**i])
pt.sort()
plt.plot([i[0] for i in pt], [i[1] for i in pt], marker='o')
addPoint(0, 1, 'none')
addPoint(p0, 1-p1, '$(p_0, 1-p_1)$')
addPoint(1-(1-p0)**2, (1-p1)**2, '$(1-(1-p_0)^2, (1-p_1)^2)$')
addPoint(1-(1-p0)**3, (1-p1)**3, '$(1-(1-p_0)^3, (1-p_1)^3)$')
addPoint(1, 0, 'none')
plt.xlabel('$\pi_{1|0}$')
plt.ylabel('$\pi_{0|1}$')
plt.legend()
plt.savefig('1b.png')
plt.show()
