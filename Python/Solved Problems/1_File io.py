f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

write = open("demo.txt", "w")
data = write.write("This is write mode")
print(data)
write.close()

append = open("demo.txt", "a")
data = append.write("\nThis is append2 mode")
print(data)
append.close()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)