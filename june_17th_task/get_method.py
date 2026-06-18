phonebook = {
    'Alice': '9876543210',
    'Bob': '8765432109'
}

print(phonebook.get('Alice'))
print(phonebook.get('Carol'))
print(phonebook.get('Carol', 'Not Found'))