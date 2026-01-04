def common():
    str1 = input("Enter a first string: ")
    str2 = input("Enter a second string: ")
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2   # Intersection or common
    print(lst)


common()