first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if first_number == second_number:
    print("Both numbers are Equal")
else:
    print("Numbers are Not Equal")

if first_number > second_number:
    print(f"Greater Number: {first_number}")
elif second_number > first_number:
    print(f"Greater Number: {second_number}")
else:
    print("Both numbers are the same")