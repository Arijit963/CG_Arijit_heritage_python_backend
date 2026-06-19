basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10

gross_salary = basic_salary + hra + da

print(f"Basic Salary : {basic_salary}")
print(f"HRA          : {hra}")
print(f"DA           : {da}")
print(f"Gross Salary : {gross_salary}")