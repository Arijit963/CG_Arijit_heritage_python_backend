emails = set()

for i in range(5):
    email = input("Enter Email: ")
    emails.add(email)

print("\nUnique Emails:")

for email in emails:
    print(email)