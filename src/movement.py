from abc import ABC, abstractmethod
from typing import Protocol

from src.core import Vector


class Movable(ABC):
    """
    Interface for all object capable of linear movement
    """

    @property
    @abstractmethod
    def position(self) -> Vector:
        ...

    @position.setter
    @abstractmethod
    def position(self, value: Vector):
        ...

    @property
    @abstractmethod
    def velocity(self) -> Vector:
        ...


class Movable2(ABC):

    """
    Interface for all object capable of linear movement
    """

    @abstractmethod
    def get_position(self) -> Vector:
        ...

    @abstractmethod
    def set_position(self, value: Vector):
        ...

    @abstractmethod
    def get_velocity(self) -> Vector:
        ...


class MoveCommand:
    """
    Executes linear movement of a Movable object
    """

    def __init__(self, movable: Movable):
        self._movable = movable

    def execute(self):
        self._movable.position = self._movable.position + self._movable.velocity


class MoveCommand2:
    """
    Executes linear movement of a Movable object
    """

    def __init__(self, movable: Movable2):
        self._movable = movable

    def execute(self):
        self._movable.set_position(
            self._movable.get_position() + self._movable.get_velocity()
        )


if __name__ == "__main__":
    pass
