dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 8, 'f': 8}


max_value = max(dict1.values())

found = {key for key,value in dict1.items() if value == max_value}

print(found)


for key,value in dict1.items():
    if value == max_value:
        print({key})