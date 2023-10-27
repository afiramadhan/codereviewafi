def even_sum(n):
    fibo = [1, 1]  # create an initial fibo with 2 items
    i = 0  # i is the number of item in fibo list
    even = []  # create a list for collecting the even number of fibo
    while fibo[-1] < n:  # make sure the last term of the list is less than n
        fibo.append(fibo[-2] + fibo[-1])  # the new item in fibo is the sum of last 2 term
    for i in range(len(fibo)):
        if fibo[i] % 2 == 0 and fibo[i] <= n:  # collect the even items which are less and equal to n
            even.append(fibo[i])
    return sum(even)
