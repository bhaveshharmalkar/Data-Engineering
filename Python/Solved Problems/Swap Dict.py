org_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

swap_dict = {value: key for key, value in org_dict.items()}

print("Original Dict: ",org_dict)
print("After Swapping: ",swap_dict)