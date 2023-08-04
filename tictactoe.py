from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
import game

class IPlayer(ABC):

	@abstractmethod
	def getMark(self) -> str:
		pass

class IMove(ABC):

	@abstractmethod
	def getPosition(self) -> tuple[int, int]:
		pass

class IGame(game.IGame[IMove]):
	
	@abstractmethod
	def addPlayer(self, player: IPlayer) -> None:
		pass

	@abstractmethod
	def createMove(self, x: int, y: int) -> IMove:
		pass

	@abstractmethod
	def hasEnded(self) -> bool:
		pass

	@abstractmethod
	def hasDrawn(self) -> bool:
		pass

	@abstractmethod
	def hasWon(self, player: IPlayer) -> bool:
		pass

	@abstractmethod
	def hasLost(self, player: IPlayer) -> bool:
		pass

class IGameFactory(game.IGameFactory[IMove]):

	@abstractmethod
	def createGame(self) -> IGame:
		pass