marks = int(input("Enter marks: "))
if marks > 100:
    print("Wrong Input")
elif marks > 89:
    print("Grade O")
elif marks > 79:
    print("Grade E")
elif marks > 69:
    print("Grade A")
elif marks > 59:
    print("Grade B")
elif marks > 49:
    print("Grade C")
elif marks > 39:
    print("Grade D")
else:
    print("Fail")