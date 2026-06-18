numbers = []

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))