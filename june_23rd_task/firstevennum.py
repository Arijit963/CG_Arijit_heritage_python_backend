def first_even(arr):

    for num in arr:

        if num % 2 == 0:
            return num

    return None


print(first_even([1, 3, 5, 8, 11]))