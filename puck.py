import numpy as np

class Puck:

    def __init__(self, position, id):
        self.position = position
        self.parking_spot = None
        self.work_status = False
        self.id = id

    def calculate_distance(self, coordinates):
        #calculates the euclidean distance between current position and another set of coordinates
        x1 = self.position[0]
        y1 = self.position[1]
        
        x2 = coordinates[0]
        y2 = coordinates[1]

        distance = np.sqrt((x2-x1)**2+(y2-y1)**2)

        return distance

    def move_to_parking_spot(self, parking_spots):
        #moves the puck from its initial state into the nearest empty parking spot
        min_distance = np.inf
        parking_spot = None

        for spot in parking_spots:
            if spot.isempty() == True: #Make sure spot is empty before calculating distance
                distance = self.calculate_distance(spot.position)
                if distance < min_distance:
                    min_distance = distance
                    parking_spot = spot
        
        self.position = parking_spot.position #Moves puck into the parking spot
        self.parking_spot = parking_spot #Changes the associated parking spot to the parking spot
        parking_spot.fill(self) #Marks the newly occupied spot as full
    
    def move_to_next_spot(self):
        #Checks that the next parking spot is empty, then moves the puck from current spot to next spot
        assert self.parking_spot.neighbor.isempty() == True
        self.position = self.parking_spot.neighbor.position
        self.parking_spot.empty() #Marks current spot as empty before it moves
        self.parking_spot = self.parking_spot.neighbor #Moves to next spot
        self.parking_spot.fill(self) #Marks new current spot as full

    def Work(self):
        #Black box work function
        self.work_status = True

    def pop(self):
        #Remove puck from queue while work is being done
        self.parking_spot.empty()
        self.parking_spot = None
        self.position = None

    def reenter_queue(self, spot):
        self.parking_spot = spot
        spot.fill(self)
        self.position = spot.position
