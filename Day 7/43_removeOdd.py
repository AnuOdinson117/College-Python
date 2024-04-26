a = set()
n = int(input("Enter length of set: "))
for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    a.add(x)

for i in range(n + 1):
    if i % 2 != 0:
        a.remove(i)

print("New Set:", a)