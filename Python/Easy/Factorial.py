n = int(input("Enter a number: "))

# 5! = 5 * 4 * 3 * 2 * 1 = 120

count = 1
fact = 1

while count <= n:
    fact = fact * count
    
    count += 1

print(fact)

    