lst = [1, 2, 21, 89, 4, 9, 19]

user = int(input("Enter number value: "))

if user not in lst:
    print(-1)
else:
    for i in lst:
        if i == user:
            print(lst.index(user))

