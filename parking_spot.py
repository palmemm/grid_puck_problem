class ParkingSpot:
    def __init__(self, position, queue_idx, neighbor):
        self.position = position #coordinates on the grid
        self.status = 'empty' #Puck status - full or empty
        self.queue_idx = queue_idx #index in the queue - 0 at END, 8 at START
        self.neighbor = neighbor #the following parking spot
        self.puck = None #Puck that occupies the spot. None if no puck is occupying the spot
    
    def isempty(self):
        #Checks if the parking spot status is empty, returns True if empty
        if self.status == 'empty':
            return True
        return False
    
    def fill(self, puck):
        #changes the status of an empty parking spot to full. 
        assert self.status == 'empty'
        self.status = 'full'
        self.puck = puck

    def empty(self):
        #changes status of a full parking spot to empty.
        assert self.status == 'full'
        self.status = 'empty'
        self.puck = None

    