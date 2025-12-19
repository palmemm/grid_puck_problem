# grid_puck_problem
## Take home challenge for Tensentric interview

#### In this project, a group of Pucks are moved through a system simulating a manufacturing line. 
#### The line exists on a grid with designated sites for the Pucks to occupy, called Parking Spots.
#### Pucks are initially placed on the grid at random points. They are then moved into the nearest Parking Spot. To improve manufacturing efficiency, Pucks are moved so that there are no gaps between any two pucks. When the Pucks are in a continuous line, work on each Puck can begin. The Puck in the top spot is moved in to the portion of the line where work is done, and the following Pucks move up the queue. After work is done, the Puck re-enters the queue at the rear, and moves up to the next empty spot. The process continues until all Pucks have had the work completed. 
#### This project simulates this process through the implementation of three classes, Puck, ParkingSpot, and Simulator. The Puck class handles Puck movements, the ParkingSpot class tracks the contents of each Parking Spot, and the Simulator coordinates the movement of a random set of pucks through the system. 

## Files:
#### puck.py - contains the Puck class
#### parking_spot.py - contains the Parking Spot class
#### simulator.py - contains the Simulator class - calls on both puck and parking_spot
#### compile.py - code to run the Simulator and assess console output

## Tests:
#### test_puck.py - contains unit tests for the Puck class
#### test_parking_spot.py - contains unit tests for the ParkingSpot class
#### test_simulator.py - contains unit tests for the Simulator class and full process tests
