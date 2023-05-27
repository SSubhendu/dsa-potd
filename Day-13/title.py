
# print the frequency of each character in a give string

str = 'my name is John Doe'
freq = {}
for char in str:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
    
print(freq)
