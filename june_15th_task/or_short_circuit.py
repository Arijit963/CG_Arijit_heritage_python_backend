
# or short-circuits when LEFT is True 

user_input = 'admin' 

 

if user_input == 'admin' or user_input == 'superuser': 

    print('Access granted') 

 

# Default value pattern using or 

name = '' 

display_name = name or 'Guest' 

print(f'Hello, {display_name}!') 

