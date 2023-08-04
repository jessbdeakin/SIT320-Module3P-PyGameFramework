
import game
import chess, backgammon, tictactoe as ttt
import mytictactoe as myttt

class MinimaxStrategy(game.IStrategy[game.GameT, game.MoveT]):
	
	def evaluateMinimax(self, g: game.GameT) -> float:
		
		moveSet: game.MoveT = g.getPossibleMoves()

		if len(moveSet) == 0:
			return [None, g.scoreState()]

		moveScores = [None]*len(moveSet)
		
		for moveIndex, move in enumerate(moveSet):
			g.makeMove(move)
			moveScores[moveIndex] = -self.evaluateMinimax(g)[1]
			g.unmakeMove(move)

		moveScore = max(moveScores)

		move = moveSet[moveScores.index(moveScore)]

		return (move, moveScore)

	def chooseMove(self, g: game.GameT) -> game.MoveT:
		
		return self.evaluateMinimax(g)[0]

class HumanTTTStrategy(game.IStrategy[ttt.IGame, ttt.IMove]):

	def chooseMove(self, g: ttt.IGame) -> ttt.IMove:

		y = int(input("Row: "))
		x = int(input("Column: "))

		return g.createMove(x, y)

###############################################################

gf: game.IGameFactory = myttt.GameFactory()
g: game.IGame = gf.createGame()

s: list[game.IStrategy[ttt.IGame, ttt.IMove]] = [
	HumanTTTStrategy(),
	MinimaxStrategy[ttt.IGame, ttt.IMove]()
]

while len(g.getPossibleMoves()) > 0:
	
	g.printState()

	g.makeMove(s[g.getTurn()].chooseMove(g))

g.printState()