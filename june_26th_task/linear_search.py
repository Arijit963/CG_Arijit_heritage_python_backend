def linear_search(arr, key):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons

    return -1, comparisons

arr = [10, 20, 30, 40, 50]
key = 40
index, comparisons = linear_search(arr, key)
print("Index:", index)
print("Comparisons:", comparisons)
