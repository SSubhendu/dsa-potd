# 27. remove special characters from a string
str = "@hello !!, how are you ?"

special = "@!?#,"
for char in str:
    if char in special:
        str = str.replace(char, "")
print(str)