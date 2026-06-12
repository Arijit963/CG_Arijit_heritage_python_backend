first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
print(f"Generated Email: {email}")