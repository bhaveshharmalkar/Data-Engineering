dict1 = {'a':1, 'b':3, 'c':8, 'z':10}
dict2 = {'e':1, 'b':9, 'f':8, 'z':5}

dict3 = {}

for char in dict1.keys():
    if char in dict2.keys():
        val1 = dict1[char]
        val2 = dict2[char]

        dict3[char] = val1 + val2
    else:
        val = dict1[char]
        dict3[char] = val

for char in dict2.keys():
    if char not in dict3.keys():
        val = dict2[char]
        dict3[char] = val

print(dict3)
