def find_topper(students):

    topper = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

    return topper


students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 88}
]

print(find_topper(students))