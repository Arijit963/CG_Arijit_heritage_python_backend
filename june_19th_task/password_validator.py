correct_password = "python123"
attempts = 0

while attempts < 5:
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful")
        break

    attempts += 1
    print(f"Incorrect Password. Attempts Left: {5 - attempts}")

else:
    print("Account Locked")