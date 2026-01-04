a = [1, 2, 3]
b = ['a', 'b', 'c']

c = []

count = 0

for i in range(len(a)):
    c.append(a[count])
    c.append(b[count])
    count = count + 1

print(c)