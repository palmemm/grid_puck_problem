from simulator import Simulator

def complete_simulation(simulation):
    simulation.initialize_pucks()
    simulation.initialize_parking_spots()
    simulation.move_pucks_to_parking_spots()
    simulation.close_parking_gaps()
    simulation.move_pucks_through_system()


simulation = Simulator()

complete_simulation(simulation)