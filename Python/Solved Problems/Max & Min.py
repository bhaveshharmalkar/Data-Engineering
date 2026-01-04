lst = [1, 3, 0, 12]
sort = sorted(lst)

print(f'Smallet Number is: {sort[0]}')
print(f'Largest Number is: {sort[-1]}')


numbers = [12, 5, 7, 25, 3, 18]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest number:", smallest)
print("Largest number:", largest)
