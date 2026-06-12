username = input("Enter your username:")

#lowercase and extra spaceremoval 
formatted_username = username.replace(" ", "").lower()
print("Formatted username:", formatted_username)
print(f"length: {len(formatted_username)}")
