import unittest
from puck import Puck
from simulator import Simulator

class TestSimulator(unittest.TestCase):
    def test_initialization(self):
        simulator = Simulator()

        self.assertFalse(hasattr(simulator, 'pucks'))
        self.assertFalse(hasattr(simulator, 'parking_spots'))
    
    def test_initialize_pucks(self):
        simulator = Simulator()
        simulator.initialize_pucks()

        self.assertLessEqual(len(simulator.pucks), 9) #Check there are less than or equal to 9 pucks
        self.assertGreater(len(simulator.pucks), 0) #Check there is at least 1 puck

        for puck in simulator.pucks:
            self.assertLessEqual(puck.position[0], 480)
            self.assertGreaterEqual(puck.position[0], 0)
            self.assertLessEqual(puck.position[1], 480)
            self.assertGreaterEqual(puck.position[1], 0)


    def test_initialize_parking_spots(self):
        simulator = Simulator()
        simulator.initialize_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]

        for i,spot in enumerate(simulator.parking_spots):
            self.assertEqual(parking_spots[i], spot.position) #Check that the parking spot coordinates match the coordinator spots
            self.assertEqual(spot.queue_idx, i)
            self.assertTrue(spot.isempty())
            self.assertIsNone(spot.puck)
    
    def test_spot_neighbors(self):
        simulator = Simulator()
        simulator.initialize_parking_spots()
        
        self.assertIsNone(simulator.parking_spots[0].neighbor)
        
        for i in range(1, len(simulator.parking_spots)):
            self.assertEqual(
                simulator.parking_spots[i].neighbor, 
                simulator.parking_spots[i-1]
            )

    def test_move_pucks_to_parking_spots(self):
        simulator = Simulator()
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        parking_spots = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        n_pucks = len(simulator.pucks)
        
        for puck in simulator.pucks:
            self.assertEqual(puck.parking_spot.status, 'full') #Check that each puck's parking spot says it is full
            self.assertFalse(puck.parking_spot.isempty())
            self.assertIsNotNone(puck.parking_spot)
            self.assertIn(puck.position, parking_spots) #Check that each puck's position is in a parking spot
            self.assertEqual(puck.position, puck.parking_spot.position)
            self.assertEqual(puck.parking_spot.puck, puck)

        filled_spots = [spot for spot in simulator.parking_spots if not spot.isempty()]
        self.assertEqual(len(filled_spots), n_pucks)

    def test_close_parking_gaps(self):
        simulator = Simulator()
        simulator.initialize_parking_spots()

        puck1 = Puck((420, 300), 0)
        puck2 = Puck((180, 180), 1)
        puck3 = Puck((180, 60), 2)
        puck1.enter_queue(simulator.parking_spots[1])
        puck2.enter_queue(simulator.parking_spots[3])
        puck3.enter_queue(simulator.parking_spots[8])

        self.assertFalse(simulator.parking_spots[1].isempty())
        self.assertTrue(simulator.parking_spots[5].isempty())

        simulator.close_parking_gaps()

        self.assertFalse(simulator.parking_spots[0].isempty())
        self.assertFalse(simulator.parking_spots[1].isempty())
        self.assertFalse(simulator.parking_spots[2].isempty())

        for i in range(3, 9):
            self.assertTrue(simulator.parking_spots[i].isempty())
    
    def test_move_pucks_through_system(self):
        simulator = Simulator()
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        simulator.close_parking_gaps()
        simulator.move_pucks_through_system()
        n_pucks = len(simulator.pucks)

        for puck in  simulator.pucks:
            self.assertEqual(puck.work_status, True)
        for i in range(n_pucks):
            self.assertFalse(simulator.parking_spots[i].isempty())
        for i in range(n_pucks, 9):
            self.assertTrue(simulator.parking_spots[i].isempty())

        for puck in simulator.pucks:
            self.assertIsNotNone(puck.parking_spot)
            self.assertEqual(puck.position, puck.parking_spot.position)

    def test_full_simulation_workflow(self):
        simulator = Simulator()
        
        simulator.initialize_pucks()
        simulator.initialize_parking_spots()
        simulator.move_pucks_to_parking_spots()
        simulator.close_parking_gaps()
        simulator.move_pucks_through_system()
        
        n_pucks = len(simulator.pucks)
        
        for puck in simulator.pucks:
            self.assertTrue(puck.work_status)
        
        filled = sum(1 for spot in simulator.parking_spots if not spot.isempty())
        self.assertEqual(filled, n_pucks)
        
        for i in range(n_pucks):
            self.assertFalse(simulator.parking_spots[i].isempty())