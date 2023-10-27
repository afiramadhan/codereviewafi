def even_sum(n):
    # Initialise values
    sum_even_fib = 0
    fib_minus = 1
    fib_current = 1
    
    # Loop until finished
    while (fib_minus + fib_current) <= n:

        # Get next number
        fib_plus = fib_minus + fib_current

        # Update
        fib_minus = fib_current
        fib_current = fib_plus

        # Get sum
        if fib_plus % 2 == 0:
            sum_even_fib += fib_plus
  
    return sum_even_fib
