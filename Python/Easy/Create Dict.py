dict = {"name":"Bhavesh", 
        "Age":24,
        "Grade":"A+"}

print(dict["Grade"])

dict["Grade"] = "O"

dict["Single"] = "Yes"

print(dict)

for i in dict.items():
    print(f"{i[0]} : {i[1]}")


for i in dict.items():
    if "name" in i[0]:
        print("yes")
        break
    else:
        print("No")
        break