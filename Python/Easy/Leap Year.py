user = int(input("Enter year: "))

if (user % 100 == 0):
    if (user % 400 == 0):
        print(f"{user} is a leap year")
    else:
        print(f"{user} is not a leap year")
elif (user % 4 == 0):
    print(f"{user} is a leap year")
else:
    print(f"{user} is not a leap year")
