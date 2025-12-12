import unittest
from parking_spot import ParkingSpot
from coordinator import Coordinator

class TestParkingSpot(unittest.TestCase):
    def test_isempty(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        self.assertTrue(spot.isempty())
        spot.status = 'full'
        self.assertFalse(spot.isempty())
    
    def test_fill(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        spot.fill()
        self.assertFalse(spot.isempty())
    
    def test_empty(self):
        spot = ParkingSpot(position=(420,180),queue_idx=5,neighbor=None)
        spot.fill()
        spot.empty()
        self.assertTrue(spot.isempty())

    