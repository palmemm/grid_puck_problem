import unittest
from parking_spot import ParkingSpot
from simulator import Simulator
from puck import Puck

class TestParkingSpot(unittest.TestCase):
    def test_init(self):
        neighbor_spot = ParkingSpot(position=(300, 180), queue_idx=4, neighbor=None)
        spot = ParkingSpot(position=(420, 180), queue_idx=5, neighbor=neighbor_spot)
        
        self.assertEqual(spot.position, (420, 180))
        self.assertEqual(spot.queue_idx, 5)
        self.assertEqual(spot.status, 'empty')
        self.assertIsNone(spot.puck)
        self.assertEqual(spot.neighbor, neighbor_spot)
    
    def test_isempty_empty(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)

        self.assertTrue(spot.isempty())
        
    def test_isempty_full(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        puck = Puck((420, 180), 0)
        spot.fill(puck)

        self.assertFalse(spot.isempty())
    
    def test_fill(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        puck = Puck((420, 180,), 0)
        spot.fill(puck)
        
        self.assertFalse(spot.isempty())
        self.assertEqual(spot.status, 'full')
        self.assertEqual(spot.puck, puck)
    
    def test_fill_when_full(self):
        spot = ParkingSpot(position=(420, 180), queue_idx=5, neighbor=None)
        puck1 = Puck((420, 180), 0)
        puck2 = Puck((420, 180), 1)
        spot.fill(puck1)

        with self.assertRaises(AssertionError):
            spot.fill(puck2)

    def test_empty(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        puck = Puck((420, 180), 0)
        spot.fill(puck)
        spot.empty()

        self.assertTrue(spot.isempty())
        self.assertEqual(spot.status, 'empty')
        self.assertIsNone(spot.puck)

    def test_empty_when_empty(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)

        with self.assertRaises(AssertionError):
            spot.empty()

    