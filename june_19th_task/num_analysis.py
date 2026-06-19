numbers = []

for i in range(10):
    num = int(input(f"Enter Number {i + 1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)
print("Even Count:", even_count)