number = int(input("Enter two digit number: "))
remainder = number % 10
sums = int(number / 10)
number = remainder * 10 + sums
print("Reverse number:", number)