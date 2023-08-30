from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
import game

class IMove(ABC):
	pass

class IPlayer(ABC):
	pass

class IGame(game.IGame[IMove]):
	pass

class IGameFactory(game.IGameFactory[IMove]):

	@abstractmethod
	def createGame(self) -> IGame:
		pass