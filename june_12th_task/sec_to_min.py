total_seconds = int(input("Enter total seconds: "))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")