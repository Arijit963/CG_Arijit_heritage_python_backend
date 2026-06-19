employees = [
    ("Rahul", "IT"),
    ("Priya", "HR"),
    ("Amit", "IT"),
    ("Sneha", "Finance"),
    ("Rohan", "HR")
]

department_count = {}

for name, department in employees:

    department_count[department] = (
        department_count.get(department, 0) + 1
    )

print("Department Wise Employee Count:")

for department, count in department_count.items():
    print(department, ":", count)