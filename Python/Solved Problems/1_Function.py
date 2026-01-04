def avg_num(a, b, c):
    return (a+b+c)/3

avg = avg_num(1, 2, 3)
print(avg)


user = int(input("Enter a Number: "))

def even_odd(user):
    if (user % 2) == 0:
        print(f'{user} is a Even number.')
    else:
        print(f'{user} is a Odd number.')

even_odd(user)


n = 5

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(n)