import unittest
from unittest import TestCase
from unittest.mock import Mock

from src.core import Vector
from src.movement import Movable, MoveCommand, Turnable, TurnCommand


class FakeMovable(Movable):
    _position: Vector = Vector([0.0, 0.0])
    _velocity: Vector = Vector([0.0, 0.0])

    def get_position(self) -> Vector:
        return self._position

    def set_position(self, value: Vector):
        self._position = value

    def get_velocity(self) -> Vector:
        return self._velocity


class MoveCommandTestCase(TestCase):
    def test_move_sucessful(self):
        body = FakeMovable()
        body._position = Vector([12.0, 5.0])
        body._velocity = Vector([-7, 3])

        MoveCommand(body).execute()
        self.assertTrue(body.get_position() == Vector([5, 8]))

    def test_move_raises_when_get_position_is_not_implemented(self):
        body = Mock(spec_set=Movable)

        body.get_position.side_effect = NotImplementedError()
        self.assertRaises(Exception, MoveCommand(body).execute)

    def test_move_raises_when_get_velocity_is_not_implemented(self):
        body = Mock(spec_set=Movable)

        body.get_velocity.side_effect = NotImplementedError()
        self.assertRaises(Exception, MoveCommand(body).execute)

    def test_move_raises_when_set_position_is_not_implemented(self):
        body = Mock(spec_set=Movable)

        body.set_position.side_effect = NotImplementedError()
        self.assertRaises(Exception, MoveCommand(body).execute)


class FakeTurnable(Turnable):
    _direction: int = 0
    _angular_velocity: int = 0
    _max_directions: int = 100

    def get_direction(self) -> int:
        return self._direction

    def set_direction(self, value: int):
        self._direction = value

    def get_angular_velocity(self) -> int:
        return self._angular_velocity

    def get_direction_max(self) -> int:
        return self._max_directions


class TurnCommandTestCase(unittest.TestCase):
    def test_start_at_zero_turn_half_circle_get_to_half_circle(self):
        body = FakeTurnable()
        body._angular_velocity = 5
        body._max_directions = 10

        TurnCommand(body).execute()
        self.assertEqual(body.get_direction(), 5)

    def test_start_at_zero_turn_by_3_half_circles_get_to_half_circle(self):
        body = FakeTurnable()
        body._angular_velocity = 15
        body._max_directions = 10

        TurnCommand(body).execute()
        self.assertEqual(body.get_direction(), 5)

    def test_start_at_nonzero_turn_full_circle_get_back_to_start(self):
        body = FakeTurnable()
        body._direction = 2
        body._angular_velocity = 10
        body._max_directions = 10

        TurnCommand(body).execute()
        self.assertEqual(body.get_direction(), 2)

    def test_turn_raises_when_get_direction_is_not_implemented(self):
        body = Mock(spec_set=Turnable)
        body.get_direction.side_effect = NotImplementedError()

        self.assertRaises(Exception, TurnCommand(body).execute)

    def test_turn_raises_when_set_direction_is_not_implemented(self):
        body = Mock(spec_set=Turnable)
        body.set_direction.side_effect = NotImplementedError()

        self.assertRaises(Exception, MoveCommand(body).execute)

    def test_turn_raises_when_get_velocity_is_not_implemented(self):
        body = Mock(spec_set=Turnable)
        body.get_angular_velocity.side_effect = NotImplementedError()

        self.assertRaises(Exception, MoveCommand(body).execute)

    def test_turn_raises_when_get_direction_max_is_not_implemented(self):
        body = Mock(spec_set=Turnable)
        body.get_direction_max.side_effect = NotImplementedError()

        self.assertRaises(Exception, MoveCommand(body).execute)
