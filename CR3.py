def even_sum(n):
    if n < 2:
        return 0 #because should be more than 2

    a, b = 1, 1
    even_sum = 0

    while a <= n:
        if a % 2 == 0: #to filter even from odd
            even_sum += a
        a, b = b, a + b #fibonacci

    return even_sum
