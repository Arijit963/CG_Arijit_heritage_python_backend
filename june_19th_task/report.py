subjects = {}

for i in range(3):
    subject = input("Enter Subject Name: ")
    marks = int(input("Enter Marks: "))

    subjects[subject] = marks

highest_subject = max(subjects, key=subjects.get)

print("\nSubjects:", subjects)
print("Highest Scoring Subject:", highest_subject)
print("Marks:", subjects[highest_subject])