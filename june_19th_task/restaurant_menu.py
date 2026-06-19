print("1. Burger - ₹120")
print("2. Pizza - ₹250")
print("3. Pasta - ₹180")

choice = int(input("Select Item: "))

match choice:

    case 1:
        bill = 120
        item = "Burger"

    case 2:
        bill = 250
        item = "Pizza"

    case 3:
        bill = 180
        item = "Pasta"

    case _:
        bill = 0
        item = "Invalid"

print(f"Item: {item}")
print(f"Bill: ₹{bill}")