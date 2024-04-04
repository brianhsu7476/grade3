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

oo=1e18

class ReflexAgent(Agent):
	"""
	A reflex agent chooses an action at each choice point by examining
	its alternatives via a state evaluation function.

	The code below is provided as a guide.	You are welcome to change
	it in any way you see fit, so long as you don't touch our method
	headers.
	"""


	def getAction(self, gameState: GameState):
		"""
		You do not need to change this method, but you're welcome to.

		getAction chooses among the best options according to the evaluation function.

		Just like in the previous project, getAction takes a GameState and returns
		some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
		"""
		# Collect legal moves and successor states
		legalMoves = gameState.getLegalActions()

		# Choose one of the best actions
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		"Add more of your code here if you want to"

		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState: GameState, action):
		"""
		Design a better evaluation function here.

		The evaluation function takes in the current and proposed successor
		GameStates (pacman.py) and returns a number, where higher numbers are better.

		The code below extracts some useful information from the state, like the
		remaining food (newFood) and Pacman position after moving (newPos).
		newScaredTimes holds the number of moves that each ghost will remain
		scared because of Pacman having eaten a power pellet.

		Print out these variables to see what you're getting, then combine them
		to create a masterful evaluation function.
		"""
		# Useful information you can extract from a GameState (pacman.py)
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()
		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

		"*** YOUR CODE HERE ***"
		foods=newFood.asList()
		nf=len(foods)
		ng=len(newGhostStates)
		# ghosts=[successorGameState.getGhostPosition(i+1) for i in range(ng)]
		if nf==0:
			return 0
		mn=oo
		for i in foods:
			mn=min(mn, manhattanDistance(newPos, i))
		for i in newGhostStates:
			if i.scaredTimer<1 and manhattanDistance(newPos, i.getPosition())<2:
				return -oo
		#for i in ghosts:
		#	if newGhostStates[i].scaredTimer<1 and manhattanDistance(newPos, i)<2:
		#		return -1e9
		return -mn-nf*10000
		
		# foodPos = newFood.asList()
		# foodCount = len(foodPos)
		# closestDistance = 1e6
		# for i in range(foodCount):
		# 	distance = manhattanDistance(foodPos[i],newPos) + foodCount*100
		# 	if distance < closestDistance:
		# 		closestDistance = distance
		# 		closestFood = foodPos
		# if foodCount == 0 :
		# 	closestDistance = 0
		# score = -closestDistance
		# for i in range(len(newGhostStates)):
		# 	ghostPos = successorGameState.getGhostPosition(i+1)
		# 	if manhattanDistance(newPos,ghostPos)<=1 :
		# 		score -= 1e6
		# return score #successorGameState.getScore()

def scoreEvaluationFunction(currentGameState: GameState):
	"""
	This default evaluation function just returns the score of the state.
	The score is the same one displayed in the Pacman GUI.

	This evaluation function is meant for use with adversarial search agents
	(not reflex agents).
	"""
	return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
	"""
	This class provides some common elements to all of your
	multi-agent searchers.	Any methods defined here will be available
	to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

	You *do not* need to make any changes here, but you can if you want to
	add functionality to all your adversarial search agents.  Please do not
	remove anything, however.

	Note: this is an abstract class: one that should not be instantiated.  It's
	only partially specified, and designed to be extended.	Agent (game.py)
	is another abstract class.
	"""

	def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
		self.index = 0 # Pacman is always agent index 0
		self.evaluationFunction = util.lookup(evalFn, globals())
		self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
	"""
	Your minimax agent (question 2)
	"""

	def getAction(self, gameState: GameState):
		"""
		Returns the minimax action from the current gameState using self.depth
		and self.evaluationFunction.

		Here are some method calls that might be useful when implementing minimax.

		gameState.getLegalActions(agentIndex):
		Returns a list of legal actions for an agent
		agentIndex=0 means Pacman, ghosts are >= 1

		gameState.generateSuccessor(agentIndex, action):
		Returns the successor game state after an agent takes an action

		gameState.getNumAgents():
		Returns the total number of agents in the game

		gameState.isWin():
		Returns whether or not the game state is a winning state

		gameState.isLose():
		Returns whether or not the game state is a losing state
		"""
		"*** YOUR CODE HERE ***"
		return self.dfs(gameState, 0, 0)
		#actions=gameState.getLegalActions(0)
		#return max(actions, key=lambda i:self.dfs(gameState.generateSuccessor(0, i), 0, 1))
	def dfs(self, s, d, ag):
		if d>=self.depth:
			return self.evaluationFunction(s)
		na=s.getNumAgents()
		actions=s.getLegalActions(ag)
		vals=[self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na) for i in actions]
		if d==0 and ag==0:
			return actions[max(list(range(len(vals))), key=lambda i:vals[i])]
		if len(vals):
			return (min if ag else max)(vals)
		return self.evaluationFunction(s)
		#if len(actions):
		#	return (min if ag else max)([self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na) for i in actions])
		#return self.evaluationFunction(s)

	# def maxi(self, s, d):
	# 	if s.isWin():
	# 		return oo
	# 	if s.isLose():
	# 		return -oo
	# 	if d>self.depth:
	# 		return self.evaluationFunction(s)
	# 	actions=s.getLegalActions(0)
	# 	if len(actions):
	# 		return max([self.mini(s.generateSuccessor(0, i), d) for i in actions])
	# 	return -oo
	# def mini(self, s, d):
	# 	if s.isWin():
	# 		return oo
	# 	if s.isLose():
	# 		return -oo
	# 	mn=oo
	# 	na=s.getNumAgents()
	# 	for i in range(1, na):
	# 		actions=s.getLegalActions(i)
	# 		if len(actions):
	# 			mn=min(mn, min([self.maxi(s.generateSuccessor(i, j), d+1) for j in actions]))
	# 	return mn

		

class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
	Your minimax agent with alpha-beta pruning (question 3)
	"""

	def getAction(self, gameState: GameState):
		"""
		Returns the minimax action using self.depth and self.evaluationFunction
		"""
		"*** YOUR CODE HERE ***"
		return self.dfs(gameState, 0, 0, -oo, oo)
		#actions=gameState.getLegalActions(0)
		#return max(actions, key=lambda i:self.dfs(gameState.generateSuccessor(0, i), 0, 1, ))
	def dfs(self, s, d, ag, a, b):
		if d>=self.depth:
			return self.evaluationFunction(s)
		na=s.getNumAgents()
		actions=s.getLegalActions(ag)
		v=oo if ag else -oo
		res=None
		for i in actions:
			v0=v
			v=(min if ag else max)(v, self.dfs(s.generateSuccessor(ag, i), d+1 if ag==na-1 else d, (ag+1)%na, a, b))
			if v!=v0:
				res=i
			if ag:
				if v<a:
					return v
				b=min(b, v)
			else:
				if v>b:
					return v if d else res
				a=max(a, v)
		if v==oo or v==-oo:
			return self.evaluationFunction(s)
		#if res==None:
		#	return v
		return v if (d or ag) else res

class ExpectimaxAgent(MultiAgentSearchAgent):
	"""
	  Your expectimax agent (question 4)
	"""

	def getAction(self, gameState: GameState):
		"""
		Returns the expectimax action using self.depth and self.evaluationFunction

		All ghosts should be modeled as choosing uniformly at random from their
		legal moves.
		"""
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
	"""
	Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
	evaluation function (question 5).

	DESCRIPTION: <write something here so we know what you did>
	"""
	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
