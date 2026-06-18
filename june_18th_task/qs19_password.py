password = input("Enter Password: ")

conditions = [
    len(password) >= 8,
    any(char.isupper() for char in password),
    any(char.islower() for char in password),
    any(char.isdigit() for char in password)
]

if all(conditions):
    print("Strong Password")
else:
    print("Weak Password")