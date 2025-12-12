import unittest
from puck import Puck
from coordinator import Coordinator

class TestPuck(unittest.TestCase):
    def test_puck_initialization(self):
        puck = Puck((200,400))
        self.assertEqual(puck.position[0], 200)
        self.assertEqual(puck.position[1], 400)

    def test_calculate_distance(self):
        puck = Puck((150,150))
        coordinates = (200,200)
        distance = puck.calculate_distance(coordinates=coordinates)
        self.assertAlmostEqual(distance, 70.71067811865476)
    
    def test_move_to_parking_spot(self):
        puck = Puck((250, 50))
        coordinator = Coordinator()
        coordinator.initialize_parking_spots()
        puck.move_to_parking_spot(parking_spots=coordinator.parking_spots)
        self.assertEqual(puck.parking_spot.position[0], 300)
        self.assertEqual(puck.parking_spot.position[1], 60)
        self.assertEqual(puck.position[0], 300)
        self.assertEqual(puck.position[1], 60)
        self.assertFalse(puck.parking_spot.isempty())

    def test_move_to_next_spot(self):
        puck = Puck((250, 50))
        coordinator = Coordinator()
        coordinator.initialize_parking_spots()
        puck.move_to_parking_spot(parking_spots=coordinator.parking_spots)
        parking_spot1 = puck.parking_spot
        puck.move_to_next_spot()
        parking_spot2 = puck.parking_spot
        self.assertEqual(parking_spot1.position[0], 300)
        self.assertEqual(parking_spot1.position[1], 60)
        self.assertTrue(parking_spot1.isempty())
        self.assertEqual(parking_spot2.position[0], 420)
        self.assertEqual(parking_spot2.position[1], 60)
        self.assertFalse(parking_spot2.isempty())
        self.assertEqual(puck.position[0], 420)
        self.assertEqual(puck.position[1], 60)
