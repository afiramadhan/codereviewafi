n = int(input())

mult_3 = (n % 3 == 0)
mult_5 = (n % 5 == 0)
mult_7 = (n % 7 == 0)

print('Is', n, 'a multiple of 3?', mult_3)
print('Is', n, 'a multiple of 5?', mult_5)
print('Is', n, 'a multiple of 7?', mult_7)