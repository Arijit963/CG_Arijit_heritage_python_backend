prices = {
    'apple': 40,
    'mango': 120,
    'banana': 20,
    'grape': 180
}

expensive = {
    item: price
    for item, price in prices.items()
    if price > 50
}

print(expensive)