import matplotlib.pyplot as plt
p0, p1=0.2, 0.3
pt=[]
for i in [j/10 for j in range(11)]:
	pt.append([p0+i*(1-p0), (1-i)*(1-p1)])
	pt.append([i*p0, (1-p1)+(1-i)*p1])
pt.sort()
plt.plot([i[0] for i in pt], [i[1] for i in pt])
plt.scatter([0, p0, 1], [1, 1-p1, 0], marker='o')
plt.annotate('(0, 1)', xy=(0, 1))
plt.annotate('(p_0, 1-p_1)', xy=(p0, 1-p1))
plt.annotate('(1, 0)', xy=(1, 0))
plt.show()
