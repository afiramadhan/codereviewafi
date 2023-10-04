n = int(input())
n_str = str(n)
multiple_of_3 = n % 3 
multiple_of_5 = n % 5 
multiple_of_7 = n % 7 

print("Is " + n_str + " a multiple of 3?", multiple_of_3 == 0)
print("Is " + n_str + " a multiple of 5?", multiple_of_5 == 0)
print("Is " + n_str + " a multiple of 7?", multiple_of_7 == 0)
