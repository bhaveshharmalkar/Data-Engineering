user = input("Enter string: ")

count = 0
vowels = []

for i in user:
    if i in 'aeiou':
        vowels.append(i)
        count = count + 1

print(f"Total {count} vowels in your string - {vowels}")
print(f"Unique is {len(set(vowels))} - {set(vowels)}")
