from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
import game

class IMove(ABC):
	pass

class IPlayer(ABC):
	pass

class IGame(game.IGame):
	pass

class IGameFactory(game.IGameFactory):

	@abstractmethod
	def createGame(self) -> IGame:
		pass