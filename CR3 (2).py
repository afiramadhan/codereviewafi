def even_sum(n):
    '''
    Returns the sum of the even Fibonacci numbers smaller
    than or equal to n.
    '''
    # Start a list of Fibonacci numbers
    fibo = [1, 1]
    
    # Loop until the next fibonacci value is greater than n
    while True:

        # The next fibonacci number (n + 1) is equal to the last two numbers added together
        fibo.append(fibo[-1] + fibo[-2])

        # Break the loop if we got to n
        if fibo[-1] > n:
            # Remove the last element from the list as it's greater than n, and break
            fibo = fibo[:-1]
            break

    # Loop to sum all the even numbers in the list
    sum_even_fib = 0
    for f in fibo:
        if f % 2 == 0:
            sum_even_fib += f

  
    return sum_even_fib
