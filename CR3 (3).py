def even_sum(n):
    '''
    Returns the sum of the even Fibonacci numbers smaller
    than or equal to n.
    '''
    # Check that the input argument is valid
    if not (isinstance(n, int) or isinstance(n, float)):
        raise TypeError('Please enter a numerical value for n.')

    if n <= 0:
        raise ValueError('Please choose a positive value of n.')

    # Initialise list to store the Fibonacci numbers
    fibo = [1, 1]
    
    # Loop until we reach n
    while (fibo[-1] + fibo[-2]) <= n:

        # Compute and append next Fibonacci number
        fibo.append(fibo[-1] + fibo[-2])

    # The sum of an odd number with an odd number is an even number.
    # The sum of an odd number with an even number is an odd number.
    # Since we start with [1, 1], by design the sequences goes [odd, odd, even, odd, odd, even, ...].
    # Summing all the even numbers is the same as summing every 3rd number.
    sum_even = sum(fibo[2::3])
  
    return sum_even
