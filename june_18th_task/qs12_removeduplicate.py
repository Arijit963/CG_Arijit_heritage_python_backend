numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = list(dict.fromkeys(numbers))

print("Original:", numbers)
print("Unique:", unique_numbers)