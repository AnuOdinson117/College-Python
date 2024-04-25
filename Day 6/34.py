stri = input("Enter a string: ")
v = 0
for i in stri:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        v = v + 1
print(v)