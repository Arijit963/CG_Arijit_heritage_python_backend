def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            print(f"Element found at index {i}")
            return True

    return False


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))