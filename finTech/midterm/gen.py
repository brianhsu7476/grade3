a=[]
for i in open('0.tex'):
	if i!='\n':
		a.append(i[:-1]+'\\\\')
for i in a:
	print(i)
