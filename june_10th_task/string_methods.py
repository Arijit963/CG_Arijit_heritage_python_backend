text = "hello WORLD from Python"

print(text.upper())       # HELLO WORLD FROM PYTHON
print(text.lower())       # hello world from python
print(text.title())       # Hello World From Python
print(text.capitalize())  # Hello world from python

# ✅ Original is unchanged (strings are immutable!)
print(text)               # hello WORLD from Python

# Real-world: Standardise user input for comparisons
city1 = "MUMBAI"
city2 = "mumbai"
city3 = "Mumbai"
# All three are 'equal' after normalising
print(city1.lower() == city2.lower() == city3.lower())  # True

