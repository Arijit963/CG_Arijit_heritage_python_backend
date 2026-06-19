age = int(input("Enter age: "))
ticket_type = input("Enter ticket type (Regular/VIP): ").lower()

if ticket_type == "regular":
    price = 200
elif ticket_type == "vip":
    price = 500
else:
    print("Invalid Ticket Type")
    exit()

if age < 12:
    discount = 0.50
elif age >= 60:
    discount = 0.30
else:
    discount = 0

final_price = price - (price * discount)

print(f"Final Ticket Price: ₹{final_price}")