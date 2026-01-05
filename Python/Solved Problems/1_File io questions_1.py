with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file i/o\nusing Java\nI like programming in Java.")

# Replace 'Java' with 'Python'
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    data = f.write(new_data)


# Search 'learning' is exist in file or not
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")


# Find in which line 'learning' word occurs first print -1 if word not found

def check_word():
    word = "learning"
    data = True
    line_num = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                return line_num
            line_num += 1
    return -1

print(check_word())


# Count the even numbers
count = []
with open("numbers.txt", "r") as f:
    data = f.read()

    nums = data.split(",")

    for i in nums:
        if (int(i) % 2 == 0): 
          count.append(i)

print(len(count))