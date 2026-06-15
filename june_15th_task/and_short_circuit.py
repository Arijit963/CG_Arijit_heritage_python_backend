
# and short-circuits when LEFT is False 

x = 0 

 

# Without short-circuit, this would crash (division by zero) 

# With short-circuit, the right side is never evaluated! 

if x != 0 and (10 / x) > 1: 

    print('Result is greater than 1') 

else: 

    print('Safe — no crash!') 

