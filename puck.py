import numpy as np

class Puck:

    def __init__(self, position, id):
        self.position = position #coordinates on the grid
        self.parking_spot = None #parking spot the puck currently lives in, None on initialization and during Work
        self.work_status = False #True/False if the puck has been worked on yet
        self.id = id #Puck numerical id 0-8

    def calculate_distance(self, coordinates):
        #calculates the euclidean distance between current position and another set of coordinates. 
        #If worried about collisions, could use Manhattan distance to traverse grid
        x1 = self.position[0]
        y1 = self.position[1]
        
        x2 = coordinates[0]
        y2 = coordinates[1]

        distance = np.sqrt((x2-x1)**2+(y2-y1)**2) #euclidean distance function

        return distance

    def enter_queue(self, spot):
        #brings a puck that is out of the queue into the queue at the designated spot. 
        #Used when moving pucks from initial state to parking spots and when pucks reenter the queue after work is done
        self.parking_spot = spot #move puck to designated spot
        spot.fill(self)
        self.position = spot.position

    def move_to_parking_spot(self, parking_spots):
        #moves the puck from its initial state into the nearest empty parking spot
        min_distance = np.inf #initialize the shortest distance at infinity
        parking_spot = None

        for spot in parking_spots:
            if spot.isempty() == True: #Make sure spot is empty before calculating distance
                distance = self.calculate_distance(spot.position)
                if distance < min_distance:
                    min_distance = distance
                    parking_spot = spot
        
        self.enter_queue(spot=parking_spot)
    
    def move_to_next_spot(self):
        #Checks that the next parking spot is empty, then moves the puck from current spot to next spot
        assert self.parking_spot.neighbor is not None #make sure it's not in the last spot
        assert self.parking_spot.neighbor.isempty() == True #Puck can only move there if it is truly empty
        self.position = self.parking_spot.neighbor.position
        self.parking_spot.empty() #Marks current spot as empty before it moves
        self.parking_spot = self.parking_spot.neighbor #Moves to next spot
        self.parking_spot.fill(self) #Fills new current spot

    def Work(self):
        #Black box work function, just changes status to True
        self.work_status = True

    def pop(self):
        #Remove puck from queue while work is being done
        self.parking_spot.empty()
        self.parking_spot = None
        self.position = None


