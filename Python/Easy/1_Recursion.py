print('First Example')
n = 5

def show(n):
    if (n == 0): # Base case
        return
    print(n)
    show(n-1) # Recursive function
    print('END') # Call stack remain task

show(n)


print('\nSecond Example')

n = 5

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return factorial(n - 1) * n

print(factorial(n))

print('\nThird Example')

def cal_sum(n):
    if n == 0:
        return 0
    
    return cal_sum(n-1) + n

print(cal_sum(5))


print('\nFourth Example')

def print_list(lst, idx=0):
    if (idx == len(lst)):
        return
    print(lst[idx])
    print_list(lst, idx+1)

fruits = ['Apple', 'Mango', 'Banana', 'Amala', 'Peru']

print(print_list(fruits))

# print(len(fruits))

