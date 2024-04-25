stri = input("Enter a string: ")
l = int(len(stri) / 2)
if len(stri) % 2 == 1:
    print("New String:", stri[l])
else:
    print("New String:", stri[l - 1] + stri[l])