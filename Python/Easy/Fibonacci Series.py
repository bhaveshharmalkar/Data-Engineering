def fibonacci_iterative(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

# Example: Print first 10 Fibonacci numbers
fibonacci_iterative(10) # Output: 0 1 1 2 3 5 8 13 21 34

