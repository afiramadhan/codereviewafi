import numpy as np

def Road_AfterTstep(R_old, T):
    '''
    Function that uses update rules to derive the state of the road after T steps. 
    
    Args:
    R_old:   numpy array, the initial state of the road where each element represents a cell. 
              R_old[i] is 0 if there is no car in the cell (i) and is 1 when there is a car in this cell.
    T:        Integer, number of time steps to update the road.
    
    Returns:
    R_new:   numpy array, the final state of the road after T steps
    '''
    road_length = len(R_old)
    
    for _ in range(T):
        # Create a copy of the current state to avoid updating in-place
        R_new = np.zeros(road_length, dtype=int)

        for i in range(road_length):
            next_position = (i + 1) % road_length
            # Check if the current cell has a car
            if R_old[i] == 1 and R_old[next_position] == 0:
                # Move the car to the next cell (considering periodic boundary)
                # next_position = (i + 1) % road_length
                R_new[next_position] = 1
            elif R_old[i] == 1 and R_old[next_position] == 1:
                R_new[i] = 1

        # Update the old state for the next iteration
        R_old = np.copy(R_new)

    return R_new
