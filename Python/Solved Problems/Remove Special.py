import re

user = input("Enter string: ")

clean_text = re.sub(r'[^a-zA-Z0-9]', ' ', user)

print(clean_text)