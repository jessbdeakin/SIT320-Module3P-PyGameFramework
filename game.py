from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
from typing import TypeVar, Generic

###

MoveT = TypeVar('MoveT')



class IGame(ABC, Generic[MoveT]):

	@abstractmethod
	def getTurn(self) -> int:
		pass

	@abstractmethod
	def getTurnCount(self) -> int:
		pass
	
	@abstractmethod
	def makeMove(self, move: MoveT) -> None:
		pass

	@abstractmethod
	def unmakeMove(self, move: MoveT) -> None:
		pass

	@abstractmethod
	def isLegal(self, move: MoveT) -> bool:
		pass

	@abstractmethod
	def getPossibleMoves(self) -> list[MoveT]:
		pass

	@abstractmethod
	def scoreState(self) -> float:
		pass

	@abstractmethod
	def printState(self) -> None:
		pass

GameT = TypeVar('GameT')

class IStrategy(ABC, Generic[GameT, MoveT]):
	
	@abstractmethod
	def chooseMove(self, game: GameT) -> MoveT:
		pass

class IGameFactory(ABC, Generic[MoveT]):

	@abstractmethod
	def createGame(self) -> IGame[MoveT]:
		pass