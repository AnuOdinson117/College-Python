stri = input("Enter a string of digits: ")
s = 0
for i in stri:
    s = int(i) + s
print("Sum of digits:", s)