def even_sum(n):
# The first two Fibonacci numbers are both 1, which is odd
    if n < 2:
        return 0 
# Initialize the first two Fibonacci numbers   
    a, b = 1, 1
    even_sum = 0
# Use while loop to iterate through the sequence until the current Fibonacci number exceeds n   
    while a <= n:        
        if a % 2 == 0:
# Add current Fibonacci number to even_sum if it's even
            even_sum += a 
# Update Fibonacci numbers            
        a, b = b, a + b
    return even_sum
# User input for generating output
n = int(input("Enter value of n:"))
print(f"The even_sum of", (n), "is", even_sum(n))