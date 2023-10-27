def even_sum(n):
    fib = [1, 1]  # Initializes the first two items of the Fibonacci sequence
    even_sum = 0  # Initializes the sum of even terms

    while fib[-1] <= n:
        if fib[-1] % 2 == 0:
            even_sum += fib[-1]
        fib.append(fib[-1] + fib[-2])

    return even_sum