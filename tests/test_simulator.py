import unittest
from puck import Puck
from simulator import Simulator

class TestSimulator(unittest.TestCase):
    def test_initialize_pucks(self):
        coordinator = Simulator()
        coordinator.initialize_pucks()
        self.assertLessEqual(len(coordinator.pucks), 9) #Check there are less than or equal to 9 pucks
        self.assertGreater(len(coordinator.pucks), 0) #Check there is at least 1 puck

    def test_initialize_parking_spots(self):
        simulator = Simulator()
        simulator.initialize_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        simulator_spots = simulator.parking_spots
        for i in range(len(parking_spots)):
            self.assertEqual(parking_spots[i], simulator_spots[i].position) #Check that the parking spot coordinates match the coordinator spots
    
    def test_move_pucks_to_parking_spots(self):
        simulator = Simulator()
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        for puck in simulator.pucks:
            self.assertIs(puck.parking_spot.status, 'full') #Check that each puck's parking spot says it is full
            self.assertIn(puck.position, parking_spots) #Check that each puck's position is in a parking spot

    def test_close_parking_gaps(self):
        simulator = Simulator()
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        simulator.close_parking_gaps()
        n_pucks = len(simulator.pucks)
        spots = simulator.parking_spots
        for i in range(n_pucks):
            self.assertFalse(spots[i].isempty())
    
    def test_move_pucks_through_system(self):
        simulator = Simulator()
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        simulator.close_parking_gaps()
        simulator.move_pucks_through_system()
        for puck in  simulator.pucks:
            self.assertEqual(puck.work_status, True)
        for i in range(len(simulator.pucks)):
            self.assertFalse(simulator.parking_spots[i].isempty())