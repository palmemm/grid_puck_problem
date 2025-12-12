import random
from puck import Puck
from grid import Grid
from parking_spot import ParkingSpot

class Coordinator:
    #Coordinator class will be where all components come together and the simulation is built
    def __init__(self):
        return None
    
    def initialize_pucks(self):
        #randomly determine the number of pucks between 1 and 9
        n_pucks = random.randint(1,9)
        pucks = [] #initiate a list containing the pucks
        for i in range(n_pucks):
            x_position = random.randint(0,480) #randomly assign x coordinate
            y_position = random.randint(0,480) #randomly assign y coordinate
            puck = Puck(position=(x_position,y_position)) #initiate it as a member of Puck class
            pucks.append(puck)
        
        self.pucks = pucks

    def initialize_parking_spots(self):
        #set parking spots to the given coordinates
        coordinates = [(420,300), (300,300), (180,300), (180,180), (300,180), (420,180), (420,60), (300,60), (180, 60)]
        spots = []

        for i in range(len(coordinates)):
            if i == 0:
                spot = ParkingSpot(position=coordinates[i], queue_idx=i, neighbor=None)
            else:
                spot = ParkingSpot(position=coordinates[i], queue_idx=i, neighbor=spots[-1])
            spots.append(spot)
        
        self.parking_spots = spots

    def move_pucks_to_parking_spots(self):
        #move all pucks from their starting positions to the nearest parking spot
        for puck in self.pucks:
            puck.move_to_parking_spot(self.parking_spots)
        
    def close_parking_gaps(self):
        #moves pucks so that there are no gaps between pucks in occupied parking spots
        for puck in self.pucks:
            if puck.parking_spot.neighbor is None:
                continue #should skip call for top spot
            while puck.parking_spot.neighbor.isempty():
                puck.move_to_next_spot()
                if puck.parking_spot.neighbor is None:
                    break
        
