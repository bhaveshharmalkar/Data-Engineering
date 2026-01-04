lst = [1, 2, 3, 3, 4, 5, 2, 1]

lst1 = []

for i in lst:
    if i in lst1:
        pass
    else:
        lst1.append(i)
    
print(lst1)