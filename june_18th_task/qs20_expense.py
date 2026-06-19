expenses = []

for day in range(1, 6):
    amount = float(input(f"Expense for Day {day}: "))
    expenses.append(amount)

print("\nExpense Report")
print("-" * 20)

for index, amount in enumerate(expenses, start=1):
    print(f"Day {index}: ₹{amount}")

print("-" * 20)
print(f"Total Expense: ₹{sum(expenses)}")
print(f"Average Expense: ₹{sum(expenses) / len(expenses):.2f}")