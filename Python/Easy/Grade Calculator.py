user = int(input("Enter your score: "))

if (user >= 0 and user <= 100):
    if (user > 90):
        print("A Grade")
    elif (user > 80 and user <= 90):
        print("B Grade")
    elif (user > 70 and user <= 80):
        print("C Grade")
    else:
        print("F Grade")
else:
    print("Invalid score (Must be 0-100)")