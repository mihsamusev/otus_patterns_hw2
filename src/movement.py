import abc

from src.core import Vector


class ICommand(abc.ABC):
    """
    Interface for executable command
    """

    def execute(self):
        ...


class Movable(abc.ABC):

    """
    Interface for all object capable of linear movement
    """

    @abc.abstractmethod
    def get_position(self) -> Vector:
        ...

    @abc.abstractmethod
    def set_position(self, value: Vector):
        ...

    @abc.abstractmethod
    def get_velocity(self) -> Vector:
        ...


class MoveCommand(ICommand):
    """
    Executes linear movement of a Movable object
    """

    def __init__(self, movable: Movable):
        self._movable = movable

    def execute(self):
        self._movable.set_position(
            self._movable.get_position() + self._movable.get_velocity()
        )


class Turnable(abc.ABC):
    """
    Interface for all objects capable of turning
    All directions are ints with max direction resolution
    """

    @abc.abstractclassmethod
    def get_direction(self) -> int:
        ...

    @abc.abstractclassmethod
    def get_direction_max(self) -> int:
        ...

    @abc.abstractclassmethod
    def set_direction(self, value: int):
        ...

    @abc.abstractclassmethod
    def get_angular_velocity(self) -> int:
        ...


class TurnCommand(ICommand):
    """
    Execulte turn of a Turnable object
    """

    def __init__(self, turnable: Turnable):
        self._turnable = turnable

    def execute(self):
        self._turnable.set_direction(
            (self._turnable.get_direction() + self._turnable.get_angular_velocity())
            % self._turnable.get_direction_max()
        )


if __name__ == "__main__":
    pass
