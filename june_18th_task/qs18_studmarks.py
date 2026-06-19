subjects = {
    "Python": int(input("Python Marks: ")),
    "SQL": int(input("SQL Marks: ")),
    "Linux": int(input("Linux Marks: "))
}

average = sum(subjects.values()) / len(subjects)

result = (
    "Pass"
    if all(mark >= 35 for mark in subjects.values())
    else "Fail"
)

print("\nSubjects:", subjects)
print("Average:", average)
print("Result:", result)