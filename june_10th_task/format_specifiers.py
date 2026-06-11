pi      = 3.14159265
price   = 1999.5
big_num = 1380000000

# Decimal places  →  :.Nf  (N decimal places)
print(f"Pi to 2 places: {pi:.2f}")       # 3.14
print(f"Pi to 4 places: {pi:.4f}")       # 3.1416

# Thousands separator  →  :,
print(f"Population: {big_num:,}")         # 1,380,000,000

# Both together
print(f"Price: ₹{price:,.2f}")           # ₹1,999.50

# Percentage  →  :.N%
pass_rate = 0.876
print(f"Pass rate: {pass_rate:.1%}")      # 87.6%

# Scientific notation  →  :.Ne
tiny = 0.000123
print(f"Tiny: {tiny:.2e}")               # 1.23e-04

