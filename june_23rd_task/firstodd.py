def first_odd(arr):

    for num in arr:

        if num % 2 != 0:
            return num

    return None


print(first_odd([2, 4, 6, 9, 10]))