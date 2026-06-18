marks = []

for i in range(1, 6):
    marks.append(float(input(f"Enter marks for Subject {i}: ")))

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")