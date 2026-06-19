VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"

username = input("Username: ")
password = input("Password: ")

if username == VALID_USERNAME and password == VALID_PASSWORD:
    print("Login Successful")
else:
    print("Invalid Credentials")