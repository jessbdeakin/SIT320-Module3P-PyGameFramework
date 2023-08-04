from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
import game

class IPlayer(ABC):
	pass

class IMove(ABC):

	@abstractmethod
	def getStartPosition(self) -> tuple[int, int]:
		pass

	@abstractmethod
	def getEndPosition(self) -> tuple[int, int]:
		pass

	@abstractmethod
	def getColor(self) -> str:
		pass

class IGame(game.IGame[IMove]):
	pass

class IGameFactory(game.IGameFactory[IMove]):

	@abstractmethod
	def createGame(self) -> IGame:
		pass