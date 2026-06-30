def lowest_grade(students):

    lowest = students[0]

    for student in students:

        if student["marks"] < lowest["marks"]:
            lowest = student

    return lowest

students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 88}
]

print(lowest_grade(students))