attendance = ("P", "P", "A", "P", "P", "A", "P")

present_days = attendance.count("P")

percentage = (present_days / len(attendance)) * 100

print(f"Attendance Percentage: {percentage:.2f}%")