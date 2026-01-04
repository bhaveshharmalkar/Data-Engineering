user_1 = input("Enter 1st string: ")
user_2 = input("Enter 2nd string: ")

if set(user_1.lower()) == set(user_2.lower()):
    print(True)
else:
    print(False)
