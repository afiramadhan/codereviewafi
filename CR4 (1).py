import numpy as np

def Road_AfterTstep(R_old,T):
    '''
    Function that uses update rules to derive the state of the road after T steps. 
    
    input:
    R_old:   an integer array, which is the initial state of the road where each element represents a cell. 
              The element R_old[i] is 0 if there is no car in the cell (i) and is 1 when there is a car in this cell. 
    T:        Number of times after which the final configuration of road is returned          
    
    output:
    R_new:  an intger array, which is the final state of the road after T steps
    '''
    # Make sure R_old is a numpy array
    R_old = np.array(R_old)

    # Make sure T is a positive integer
    T = int(T)
    
    # Put the total number of cells in variable N
    N = np.shape(R_old)[0]
    
    # Form the output array with the same shape as R_old. Fill it initially with zeros. Make sure it is integer
    R_new = np.zeros_like(R_old, dtype=int)
    
    # Loop over T time steps
    for j in range(T):
        
        # Loop over each cell and update its value using the update rules
        for i in range(N):
            if R_old[i] == 1:
                # To take care of the bounday condition: 
                # create i_plus1 such that when i is N-1 (i.e. in last cell), instead of index (i+1) we use index (0)
                i_plus1 = (i+1) % N
                R_new[i] = R_old[i_plus1]
                
            else:
                # Note: python takes care of the other boundary condition automatically as R_old[-1] to is the last element of R_old
                R_new[i] = R_old[i-1]
        
        # Update the array for the next time step
        R_old[:] = R_new[:]
        
    return R_new
