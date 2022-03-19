from unittest import TestCase
from unittest.mock import Mock

from src.core import Vector
from src.movement import Movable, Movable2, MoveCommand, MoveCommand2


class MockMovable(Movable2):
    _position: Vector
    _velocity: Vector

    def get_position(self) -> Vector:
        return self._position

    def set_position(self, value: Vector):
        self._position = value

    def get_velocity(self) -> Vector:
        return self._velocity


class MoveTestCase(TestCase):
    def test_move_sucessful(self):
        body = Mock(spec_set=Movable)
        body.position = Vector([12.0, 5.0])
        body.velocity = Vector([-7, 3])

        MoveCommand(body).execute()
        self.assertTrue(body.position == Vector([5, 8]))

    def test_move_sucessful2(self):
        body = MockMovable()
        body._position = Vector([12.0, 5.0])
        body._velocity = Vector([-7, 3])
        MoveCommand2(body).execute()

        self.assertTrue(body.get_position() == Vector([5, 8]))

    def test_move_raises_when_get_position_is_not_implemented(self):
        body = Mock(spec_set=Movable2)
        body.get_position.side_effect = NotImplementedError()
        body.get_velocity.return_value = Vector([-5.0, 3.0])

        self.assertRaises(NotImplementedError, MoveCommand2(body).execute)

    def test_move_raises_when_get_velocity_is_not_implemented(self):
        body = Mock(spec_set=Movable2)
        body.get_position.return_value = Vector([12.0, 5.0])
        body.get_velocity.side_effect = NotImplementedError()

        self.assertRaises(NotImplementedError, MoveCommand2(body).execute)

    def test_move_raises_when_set_position_is_not_implemented(self):
        body = Mock(spec_set=Movable2)
        body.get_position.return_value = Vector([12.0, 5.0])
        body.get_velocity.return_value = Vector([-5.0, 3.0])
        body.set_position.side_effect = NotImplementedError()

        self.assertRaises(NotImplementedError, MoveCommand2(body).execute)
