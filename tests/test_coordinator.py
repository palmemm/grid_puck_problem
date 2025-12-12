import unittest
from puck import Puck
from coordinator import Coordinator

class TestCoordinator(unittest.TestCase):
    def test_initialize_pucks(self):
        coordinator = Coordinator()
        coordinator.initialize_pucks()
        self.assertLessEqual(len(coordinator.pucks), 9) #Check there are less than or equal to 9 pucks
        self.assertGreater(len(coordinator.pucks), 0) #Check there is at least 1 puck

    def test_initialize_parking_spots(self):
        coordinator = Coordinator()
        coordinator.initialize_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        coordinator_spots = coordinator.parking_spots
        for i in range(len(parking_spots)):
            self.assertEqual(parking_spots[i], coordinator_spots[i].position) #Check that the parking spot coordinates match the coordinator spots
    
    def test_move_pucks_to_parking_spots(self):
        coordinator = Coordinator()
        coordinator.initialize_pucks()
        coordinator.initialize_parking_spots()
        coordinator.move_pucks_to_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        for puck in coordinator.pucks:
            self.assertIs(puck.parking_spot.status, 'full') #Check that each puck's parking spot says it is full
            self.assertIn(puck.position, parking_spots) #Check that each puck's position is in a parking spot

    def test_close_parking_gaps(self):
        coordinator = Coordinator()
        coordinator.initialize_pucks()
        coordinator.initialize_parking_spots()
        coordinator.move_pucks_to_parking_spots()
        coordinator.close_parking_gaps()
        n_pucks = len(coordinator.pucks)
        spots = coordinator.parking_spots
        for i in range(n_pucks):
            self.assertFalse(spots[i].isempty())
        