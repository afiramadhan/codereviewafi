def even_sum(n):
    if n < 2:
        return 0

    a, b = 1, 1
    even_sum = 0

    while a <= n:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum
