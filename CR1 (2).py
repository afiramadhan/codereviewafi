n = int(input())


# Loop to test 3, 5, 7 one after the other
for m in [3, 5, 7]:
    
    # Starting with 0, multiply all numbers up to 1000 by m and check if they match with n
    x = 0
    while x <= 1000:
        
        # If we obtain n when we multiply the current number by m, then n is a multiple of m
        if m*x == n:
            # Print what I need and stop the loop
            print('Is ' + str(n) + ' a multiple of ' + str(m) + '? True')
            break
        
        # Go to the next number
        x = x + 1
    
    # If we got to the end of the loop and haven't found n, then it's not a multiple of m
    if x > 1000:
        print('Is ' + str(n) + ' a multiple of ' + str(m) + '? False')