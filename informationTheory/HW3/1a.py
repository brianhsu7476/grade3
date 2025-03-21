import matplotlib.pyplot as plt

def addPoint(x, y, label):
	if label=='none':
		label='$('+str(x)+', '+str(y)+')$'
	plt.annotate('  '+label, xy=(x, y))

p0, p1=0.2, 0.3
pt=[]
for i in [j/10 for j in range(11)]:
	pt.append([p0+i*(1-p0), (1-i)*(1-p1)])
	pt.append([i*p0, (1-p1)+(1-i)*p1])
pt.sort()
plt.plot([i[0] for i in pt], [i[1] for i in pt])
plt.scatter([0, p0, 1], [1, 1-p1, 0], marker='o')
addPoint(0, 1, 'none')
addPoint(p0, 1-p1, '$(p_0, 1-p_1)$')
addPoint(1, 0, 'none')
plt.xlabel('$\pi_{1|0}$')
plt.ylabel('$\pi_{0|1}$')
plt.legend()
plt.savefig('1a.png')
plt.show()
