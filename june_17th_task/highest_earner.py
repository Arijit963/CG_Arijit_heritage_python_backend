salaries = {
    'Alice': 75000,
    'Bob': 85000,
    'Carol': 70000
}

top_earner = max(salaries, key=salaries.get)

print(top_earner)