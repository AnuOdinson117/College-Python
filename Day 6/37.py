stri = input("Enter a string: ")
strrev = ""
for i in stri:
    strrev = i + strrev
print(strrev == stri)