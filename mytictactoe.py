import game, tictactoe as ttt

class Move(ttt.IMove):

	def __init__(self, position: tuple[int, int]):
		self.position = position

	def getPosition(self):
		return self.position

	def __repr__(self):
		return f"Move({self.position})"

	def __str__(self):
		return repr(self)

class Player(ttt.IPlayer):

	def __init__(self, mark: str):
		self.mark: str = mark

	def getMark(self) -> str:
		return self.mark

class Game(ttt.IGame):
	
	def __init__(self):
		self.board: list[ttt.IPlayer] = [None]*3
		for y in range(3):
			self.board[y] = [None]*3
		
		self.players: list[ttt.IPlayer] = []
		self.turn: int = 0
		pass

	def getTurn(self) -> int:
		return self.turn

	def getTurnCount(self) -> int:
		return len(self.players)

	def printState(self) -> None:
		
		print()

		if not self.hasEnded():
			print(f"Player #{self.turn}'s turn")

		print('---')

		for y in range(3):
			for x in range(3):
				if self.board[y][x] == None:
					print(' ', end='')
				else:
					print(self.board[y][x].getMark(), end='')
			print('')

		print('---')

		for playerIndex, player in enumerate(self.players):
			if self.hasWon(player):
				print(f"Player #{playerIndex} WINS")
				break
		else:
			if self.hasDrawn():
				print("DRAW")
		

	def hasDrawn(self) -> bool:

		for y in range(3):
			for x in range(3):
				if self.board[y][x] == None:
					return False

		return True

	def hasWon(self, player: ttt.IPlayer) -> bool:

		mask = [None]*3
		for y in range(3):
			mask[y] = [None]*3

		for y in range(3):
			for x in range(3):
				mask[y][x] = (self.board[y][x] == player)

		horizontal = 	(mask[0][0] and mask[0][1] and mask[0][2]) \
						or (mask[1][0] and mask[1][1] and mask[1][2]) \
						or (mask[2][0] and mask[2][1] and mask[2][2])

		vertical = 		(mask[0][0] and mask[1][0] and mask[2][0]) \
						or (mask[0][1] and mask[1][1] and mask[2][1]) \
						or (mask[0][2] and mask[1][2] and mask[2][2])

		diagonal = 		(mask[0][0] and mask[1][1] and mask[2][2]) \
						or (mask[0][2] and mask[1][1] and mask[2][0])

		return horizontal or vertical or diagonal

	def hasLost(self, player: ttt.IPlayer) -> bool:
		return not ( self.hasDrawn() or self.hasWon(player) )

	def hasEnded(self) -> bool:
		if self.hasDrawn():
			return True

		for player in self.players:
			if self.hasWon(player):
				return True
		
		return False

	def addPlayer(self, player: ttt.IPlayer) -> None:
		self.players.append(player)

	def makeMove(self, move: ttt.IMove):
		if not self.isLegal(move):
			raise Exception("Move not legal.")

		self.board[move.getPosition()[1]][move.getPosition()[0]] = self.players[self.turn]
		self.turn = (self.turn + 1) % len(self.players)

	def unmakeMove(self, move: ttt.IMove):
		self.board[move.getPosition()[1]][move.getPosition()[0]] = None
		self.turn = (self.turn - 1) % len(self.players)

	def isLegal(self, move: ttt.IMove):

		if move.getPosition()[0] <= -1 or move.getPosition()[0] >= 3:
			return False

		if move.getPosition()[1] <= -1 or move.getPosition()[1] >= 3:
			return False

		if self.board[move.getPosition()[1]][move.getPosition()[0]] != None:
			return False

		return True

	def createMove(self, x: int, y: int) -> ttt.IMove:
		return Move((x, y))

	def getPossibleMoves(self) -> list[ttt.IMove]:
		moves: list[ttt.IMove] = []

		if self.hasEnded():
			return moves

		for y in range(3):
			for x in range(3):
				move: ttt.IMove = Move((x, y))
				if self.board[y][x] == None:
					moves.append(move)

		return moves
		
	def scoreState(self) -> float:

		if self.hasWon( self.players[self.turn] ):
			return 1

		if self.hasLost( self.players[self.turn] ):
			return -1

		return 0

class GameFactory(ttt.IGameFactory):
	
	def createGame(self) -> ttt.IGame:
		game: ttt.IGame = Game()
		game.addPlayer(Player('X'))
		game.addPlayer(Player('O'))
		return game