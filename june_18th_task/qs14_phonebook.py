phonebook = {
    "Rahul": "9876543210",
    "Priya": "9123456789",
    "Amit": "9988776655"
}

name = input("Enter name to search: ")

print(phonebook.get(name, "Contact Not Found"))