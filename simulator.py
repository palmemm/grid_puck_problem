import random
from puck import Puck
from parking_spot import ParkingSpot

class Simulator:
    #Simulator class will be where all components come together and the simulation is built
    def __init__(self):
        pass
    
    def initialize_pucks(self):
        #randomly determine the number of pucks between 1 and 9
        n_pucks = random.randint(1,9)
        pucks = [] #initialize a list containing the pucks
        for i in range(n_pucks):
            x_position = random.randint(0,480) #randomly assign x coordinate
            y_position = random.randint(0,480) #randomly assign y coordinate
            print('Initial Position for Puck ', i, 'set to: ', (x_position, y_position))
            puck = Puck(position=(x_position,y_position), id=i) #initiate it as a member of Puck class
            pucks.append(puck)
        
        self.pucks = pucks #stores list of pucks within simulator class

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
        
        self.parking_spots = spots #stores list of parking spots within simulator class

    def print_config(self):
        #Helper function to visualize the configuration of the pucks
        conf = 'START -> '
        for spot in reversed(self.parking_spots):
            if spot.status == 'empty':
                conf = conf + 'EMPTY -> '
            else:
                conf = conf + 'FULL - PUCK #' + str(spot.puck.id) + ' -> '
        conf = conf + 'END'
        print(conf)

    def move_pucks_to_parking_spots(self):
        #move all pucks from their starting positions to the nearest parking spot
        for puck in self.pucks:
            puck.move_to_parking_spot(self.parking_spots)
            print('Moved puck ', puck.id, 'to parking spot ', puck.parking_spot.queue_idx, 'at: ', puck.position)
        
        print('Initial Configuration:')
        self.print_config()
        
    def close_parking_gaps(self):
        #moves pucks so that there are no gaps between pucks in occupied parking spots
        for spot in self.parking_spots: #Loop through spots because they are stored in order of closest to farthest from END
            if spot.neighbor is None:
                continue #skip call for top spot that doesn't have a Neighbor
            puck = spot.puck
            if not puck:
                continue #Skip to next spot if there is no puck in this spot
            while puck.parking_spot.neighbor.isempty():
                puck.move_to_next_spot()
                if puck.parking_spot.neighbor is None:
                    break #break the while loop if the puck's new parking spot doesn't have a neighbor (is the first spot)
            if spot.position != puck.position: #If the spot's position (from the beginning of the for loop) is different from puck (after while loop), then the puck has moved
                print('Moved Puck ', puck.id, ' to Spot ', puck.parking_spot.queue_idx)
                self.print_config()
        
        print('All Gaps Filled')

    def move_pucks_through_system(self):
        #Runs the simulator to have Work done on all pucks
        print('--------BEGIN WORK--------')
        while self.parking_spots[0].puck.work_status == False: #Perform work until the puck in the top spot is complete
            puck = self.parking_spots[0].puck
            puck.pop()
            puck.Work()
            print('Working on Puck #', str(puck.id))
            if len(self.pucks) > 1:
                self.close_parking_gaps() #Move the following pucks to the next positions

            puck.enter_queue(self.parking_spots[-1])
            print('Puck #', str(puck.id), ' Finished. Reentering Queue.')
            self.print_config()

            print('Moving Puck #', str(puck.id), ' to the first open spot')
            self.close_parking_gaps() #Move last puck to the first open spot

        print('--------END WORK--------')

        print('Final Configuration:')
        self.print_config()