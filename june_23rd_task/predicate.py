def search(collection, predicate):

    for item in collection:

        if predicate(item):
            return item

    return None


result = search(
    [10, 15, 20, 25],
    lambda x: x > 18
)

print(result)