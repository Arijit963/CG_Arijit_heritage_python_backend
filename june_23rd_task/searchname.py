def search_by_name(students, name):

    for student in students:

        if student["name"].lower() == name.lower():
            return student

    return None
students = [
    {"roll": 1, "name": "Rahul"},
    {"roll": 2, "name": "Priya"}
]
print(search_by_name(students, "Priya"))