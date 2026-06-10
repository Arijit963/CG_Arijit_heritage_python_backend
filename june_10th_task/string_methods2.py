sentence = "I love Java. Java is great."
updated  = sentence.replace("Java", "Python")
print(updated)    # I love Python. Python is great.

# Replace only first occurrence
partial  = sentence.replace("Java", "Python", 1)
print(partial)    # I love Python. Java is great.

# Real-world: Template personalisation
template = "Dear CUSTOMER_NAME, your order ORDER_ID is ready."
msg = template.replace("CUSTOMER_NAME", "Ravi").replace("ORDER_ID", "#78234")
print(msg)

# split() — breaks string into a list
csv_row  = "Arjun,25,Mumbai,Engineer"
fields   = csv_row.split(",")
print(fields)          # ['Arjun', '25', 'Mumbai', 'Engineer']
print(fields[0])       # Arjun
print(fields[2])       # Mumbai

# split on whitespace by default
sentence = "Python is fun to learn"
words    = sentence.split()
print(words)           # ['Python', 'is', 'fun', 'to', 'learn']
print(len(words))      # 5

# join() — reassembles a list back into a string
tags = ["python", "coding", "beginner", "tutorial"]
hashtags = "#" + "  #".join(tags)
print(hashtags)        # #python  #coding  #beginner  #tutorial

