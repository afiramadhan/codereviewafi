import numpy as np

def Road_AfterTstep(R_old, T):
    '''
    A function that, after T steps, determines the condition of the road using update rules. 
    
    Args:
    R_old:   numpy array, the original state of the road, where a cell is represented by each element. 
    When a car is present in this cell, R_old[i] is 1; otherwise, it is 0 when it is not.
    T:        Integer, number of time steps to update the road.
    
    Returns:
    R_new:   numpy array, the final state of the road after T steps
    '''
    road_length = len(R_old)
    
    for _ in range(T):
        #to avoid updating in-place, we firstly make a copy of the current state.

        R_new = np.zeros(road_length, dtype=int)

        for i in range(road_length):
            next_position = (i + 1) % road_length
            #then we check if the current cell has a car
            if R_old[i] == 1 and R_old[next_position] == 0:
                #we then proceed to the next cell with the car, taking into account the periodic border.
                R_new[next_position] = 1
            elif R_old[i] == 1 and R_old[next_position] == 1:
                R_new[i] = 1

        #we update the old state for the next iteration
        R_old = np.copy(R_new)

    return R_new
