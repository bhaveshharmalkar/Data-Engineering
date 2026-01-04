user = input("Enter string: ")

def palindrome(x):
    if x == x[::-1]:
        print(f"'{user}' is a palindrome")
    else:
        print(f"'{user}' is not a palindrome")

lower_case = user.lower() 
result = palindrome(lower_case.replace(" ", ""))