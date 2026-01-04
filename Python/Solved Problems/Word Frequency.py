user = input("Enter sentence: ")

split_user = user.split()

word = "the"

count = 0

for i in split_user:
    if word == i:
        count = count + 1

print(count)