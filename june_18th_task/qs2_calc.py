num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/,%,//,**): ")
num2 = float(input("Enter second number: "))

operations = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Division by zero not allowed",
    '%': num1 % num2,
    '//': num1 // num2,
    '**': num1 ** num2
}

print("Result:", operations.get(operator, "Invalid Operator"))