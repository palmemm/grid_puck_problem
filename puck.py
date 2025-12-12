import numpy as np

class Puck:

    def __init__(self, position):
        self.position = position
        self.parking_spot = None

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
        
        self.position = parking_spot.position
        parking_spot.fill()
        
