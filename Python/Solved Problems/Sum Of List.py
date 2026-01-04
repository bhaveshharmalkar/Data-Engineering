user = int(input("How many numbers you want to sum: "))

lst = []

if user == 1:
    print("Enter more than 1 values")
else:
    for i in range(1, user+1):
        user_num = int(input(f"Enter {i} number: " ))
        lst.append(user_num)

    sum = 0
    for i in lst:
        sum = sum + i

    print(f"Total of your numbers is: {sum}") 