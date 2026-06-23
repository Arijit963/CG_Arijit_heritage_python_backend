def search_by_roll(students, roll):

    for student in students:

        if student["roll"] == roll:
            return student

    return None


students = [
    {"roll": 1, "name": "Rahul"},
    {"roll": 2, "name": "Priya"}
]

print(search_by_roll(students, 2))