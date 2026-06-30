class GradeFinder:

    def __init__(self, students):
        self.students = students

    def find_by_name(self, name):

        for student in self.students:

            if student["name"].lower() == name.lower():
                return student

        return None

    def find_by_roll(self, roll):

        for student in self.students:

            if student["roll"] == roll:
                return student

        return None

    def find_topper(self):

        topper = self.students[0]

        for student in self.students:

            if student["grade"] > topper["grade"]:
                topper = student

        return topper


students = [
    {"roll": 1, "name": "Rahul", "grade": 85},
    {"roll": 2, "name": "Priya", "grade": 92},
    {"roll": 3, "name": "Amit", "grade": 78}
]

finder = GradeFinder(students)

print(finder.find_by_name("Priya"))
print(finder.find_topper())