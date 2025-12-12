class ParkingSpot:
    def __init__(self, position, queue_idx):
        self.position = position
        self.status = 'empty'
        self.queue_idx = queue_idx
    
    def isempty(self):
        if self.status == 'empty':
            return True
        return False
    
    def fill(self):
        #changes the status of an empty parking spot to full. 
        #Used when a puck fills the spot for the first time
        assert self.status == 'empty'
        self.status = 'full'

    def empty(self):
        #changes status of a full parking spot to empty.
        #used when moving the pucks from original parking spots to back-to-back spots
        assert self.status == 'full'
        self.status = 'empty'