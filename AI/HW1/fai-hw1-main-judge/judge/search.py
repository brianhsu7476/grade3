from collections import deque
from heapq import *

goals, ng=[], 0
dis=[]
n, m, lgn, lgm=0, 0, 0, 0
sx, sy=0, 0
haveKruskal={}
oo=1000000007
mz=''

def bfs0(s):
	d=[[-1 for j in range(m+1)] for i in range(n+1)]
	d[s[0]][s[1]]=0
	bfs=deque([s])
	while len(bfs)>0:
		u=bfs.popleft()
		ngh=mz.getNeighbors(u[0], u[1])
		for v in ngh:
			if d[v[0]][v[1]]==-1:
				d[v[0]][v[1]]=d[u[0]][u[1]]+1
				bfs.append(v)
	return d

def bfs1(s, t):
	d=[[-1 for j in range(m+1)] for i in range(n+1)]
	d[s[0]][s[1]]=0
	bfs=deque([s])
	par={s:s}
	t1=(-1, -1)
	while len(bfs)>0:
		u=bfs.popleft()
		ngh=mz.getNeighbors(u[0], u[1])
		for v in ngh:
			if d[v[0]][v[1]]==-1:
				d[v[0]][v[1]]=d[u[0]][u[1]]+1
				bfs.append(v)
				par[v]=u
			if v in t:
				t1=v
				bfs=deque([])
				break
	res=deque([t1])
	while res[0]!=s:
		res.appendleft(par[res[0]])
	return list(res)

def init(maze, typ):
	global goals, ng, n, m, lgn, lgm, sx, sy, dis, mz
	mz=maze
	goals=maze.getObjectives()
	ng=len(goals)
	n, m=maze.getDimensions()
	lgn, lgm=n.bit_length(), m.bit_length()
	sx, sy=maze.getStart()
	if typ:
		dis=[bfs0(i) for i in goals]

class edge:
	def __init__(self, u, v, w):
		self.u, self.v, self.w=u, v, w
	def __lt__(self, r):
		return self.w<r.w

class dsu:
	def __init__(self, n):
		self.p=list(range(n))
	def find(self, x):
		if self.p[x]==x:
			return x
		self.p[x]=self.find(self.p[x])
		return self.p[x]
	def union(self, x, y):
		rx, ry=self.find(x), self.find(y)
		self.p[rx]=ry
		return False if rx==ry else True

def kruskal(g):
	if g in haveKruskal:
		return haveKruskal[g]
	e=[]
	for i in range(ng):
		if g>>i&1:
			for j in range(i+1, ng):
				if g>>j&1:
					e.append(edge(i, j, dis[i][goals[j][0]][goals[j][1]]))
	e.sort()
	p=dsu(ng)
	res=0
	for i in e:
		if p.union(i.u, i.v):
			res+=i.w
	haveKruskal[g]=res
	return res

class state:
	def __init__(self, x, y, g, d):
		self.x, self.y, self.d=x, y, d
		for i in range(ng):
			if g>>i&1 and (x, y)==goals[i]:
				g^=1<<i
				break
		self.g=g
	def __hash__(self):
		return self.g<<(n+m)&self.x<<m&self.y
	def __eq__(self, r):
		return self.x==r.x and self.y==r.y and self.g==r.g
	def h(self):
		if len(dis)==0:
			return abs(self.x-goals[0][0])+abs(self.y-goals[0][1])
		mn=oo
		for i in range(ng):
			if self.g>>i&1:
				mn=min(mn, dis[i][self.x][self.y])
		return mn+kruskal(self.g)
	def __lt__(self, r):
		return self.d+self.h()<r.d+r.h()

def sol(maze, typ):
	init(maze, typ)
	s=state(sx, sy, (1<<ng)-1, 0)
	t=state(-1, -1, -1, -1)
	pq=[s]
	par={s:s}
	while len(pq)>0:
		u=heappop(pq)
		ngh=mz.getNeighbors(u.x, u.y)
		for v0 in ngh:
			v=state(v0[0], v0[1], u.g, u.d+1)
			if v not in par:
				heappush(pq, v)
				par[v]=u
			if v.g==0:
				t=v
				pq=[]
				break
	res=deque([t])
	while res[0]!=s:
		res.appendleft(par[res[0]])
	return [(i.x, i.y) for i in res]

def search(maze, searchMethod):
	return {
		"bfs": bfs,
		"astar": astar,
		"astar_corner": astar_corner,
		"astar_multi": astar_multi,
		"fast": fast,
	}.get(searchMethod)(maze)

def bfs(maze):
	init(maze, False)
	return bfs1(mz.getStart(), mz.getObjectives())

def astar(maze):
	return sol(maze, False)

def astar_corner(maze):
	return sol(maze, True)

def astar_multi(maze):
	return sol(maze, True)

def fast(maze):
	init(maze, False)
	s=mz.getStart()
	t=mz.getObjectives()
	res=[s]
	while len(t)>0:
		p=bfs1(s, t)
		res+=p[1:]
		s=p[-1]
		t0=t
		t=[]
		for i in t0:
			if i!=s:
				t.append(i)
	return res
