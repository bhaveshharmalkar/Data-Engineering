user = input("Enter a string: ")

dict = {}

for char in user:
    if char in dict.keys():
        val = dict[char]
        dict[char] = val + 1
    else:
        dict[char] = 1

print(dict)


