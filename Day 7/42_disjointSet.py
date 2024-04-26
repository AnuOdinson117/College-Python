a = set()
n = int(input("Enter length of set A: "))
for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    a.add(x)

b = set()
n = int(input("Enter length of set B: "))
for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    b.add(x)

if a.isdisjoint(b):
    print("They are Disjoint sets")
else:
    print("They are not Disjoint sets")