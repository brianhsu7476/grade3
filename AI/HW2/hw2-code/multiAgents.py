# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

def avg(a):
	return sum(a)/len(a)

oo=134521345213452

class ReflexAgent(Agent):
	def getAction(self, gameState: GameState):
		legalMoves = gameState.getLegalActions()
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best
		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState: GameState, action):
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()
		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
		foods=newFood.asList()
		nf, ng=len(foods), len(newGhostStates)
		if nf==0:
			return 0
		for i in newGhostStates:
			if i.scaredTimer<1 and manhattanDistance(newPos, i.getPosition())<2:
				return -oo
		return -min([manhattanDistance(newPos, i) for i in foods])-nf*10000 if nf else oo

def scoreEvaluationFunction(currentGameState: GameState):
	return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
	def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
		self.index = 0 # Pacman is always agent index 0
		self.evaluationFunction = util.lookup(evalFn, globals())
		self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
	def getAction(self, gameState: GameState):
		return self.dfs(gameState, 0, 0)
	def dfs(self, s, d, ag):
		if d>=self.depth:
			return self.evaluationFunction(s)
		na, actions=s.getNumAgents(), s.getLegalActions(ag)
		vals=[self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na) for i in actions]
		return actions[max(list(range(len(vals))), key=lambda i:vals[i])] if d==0 and ag==0 else (min if ag else max)(vals) if len(vals) else self.evaluationFunction(s)

class AlphaBetaAgent(MultiAgentSearchAgent):
	def getAction(self, gameState: GameState):
		return self.dfs(gameState, 0, 0, -oo, oo)
	def dfs(self, s, d, ag, a, b):
		if d>=self.depth:
			return self.evaluationFunction(s)
		na, actions, v, res=s.getNumAgents(), s.getLegalActions(ag), oo if ag else -oo, None
		for i in actions:
			v0=v
			v=(min if ag else max)(v, self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na, a, b))
			res=i if v!=v0 else res
			if ag:
				if v<a:
					return v
				b=min(b, v)
			else:
				if v>b:
					return v if d else res
				a=max(a, v)
		return self.evaluationFunction(s) if v==oo or v==-oo else v if d or ag else res

class ExpectimaxAgent(MultiAgentSearchAgent):
	def getAction(self, gameState: GameState):
		return self.dfs(gameState, 0, 0)
	def dfs(self, s, d, ag):
		if d>=self.depth:
			return self.evaluationFunction(s)
		na, actions=s.getNumAgents(), s.getLegalActions(ag)
		vals=[self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na) for i in actions]
		return actions[max(list(range(len(vals))), key=lambda i:vals[i])] if d==0 and ag==0 else (avg if ag else max)(vals) if len(vals) else self.evaluationFunction(s)

from collections import deque
n, m, walls, st, ghosts, foods, caps, scared=0, 0, [], (0, 0), [], [], [], 0
dg, df, dc=[], [], []

def init(s: GameState):
	global n, m, walls, st, ghosts, foods, caps, scared
	walls=s.getWalls().data
	n, m=len(walls), len(walls[0])
	st=s.getPacmanPosition()
	tmp=s.getGhostPositions()
	ghosts=[[0 for j in range(m)] for i in range(n)]
	for i in tmp:
		ghosts[round(i[0])][round(i[1])]=1
	foods=s.getFood().data
	tmp=s.getCapsules()
	caps=[[0 for j in range(m)] for i in range(n)]
	for i in tmp:
		caps[round(i[0])][round(i[1])]=1
	tmp=s.getGhostStates()
	scared=oo if len(tmp)==0 else tmp[0].scaredTimer

def allDistance():
	global dg, df, dc
	dg, df, dc=[], [], []
	d=[[-1 for j in range(m)] for i in range(n)]
	d[st[0]][st[1]]=0
	bfs=deque([st])
	while len(bfs)>0:
		u=bfs.popleft()
		ngh=[]
		nxt=[(1, 0), (0, 1), (-1, 0), (0, -1)]
		for i in nxt:
			nxx, nxy=u[0]+i[0], u[1]+i[1]
			if nxx>=0 and nxx<n and nxy>=0 and nxy<m and walls[nxx][nxy]==0:
				ngh.append((nxx, nxy))
		for v in ngh:
			if d[v[0]][v[1]]==-1:
				d[v[0]][v[1]]=d[u[0]][u[1]]+1
				bfs.append(v)
	for i in range(n):
		for j in range(m):
			if ghosts[i][j]:
				dg.append(d[i][j])
			if foods[i][j]:
				df.append(d[i][j])
			if caps[i][j]:
				dc.append(d[i][j])
	dg, df, dc=sorted(dg), sorted(df), sorted(dc)

def betterEvaluationFunction(currentGameState: GameState):
	global dg, df, dc
	init(currentGameState)
	allDistance()
	res=currentGameState.getScore()
	df+=dc
	if scared>1:
		res-=dg[0]*6
	if scared<1 and dg[0]<2:
		res-=oo
	else:
		res+=(-df[0]-len(df)*10000)*5 if len(df) else oo
	return res

better = betterEvaluationFunction
