routes = {
    frozenset({'Delhi', 'Mumbai'}): 1400,
    frozenset({'Delhi', 'Chennai'}): 2200
}

key = frozenset({'Mumbai', 'Delhi'})

print(routes[key])