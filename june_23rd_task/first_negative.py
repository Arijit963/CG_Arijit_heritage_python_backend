def first_negative(arr):

    for num in arr:

        if num < 0:
            return num

    return None


print(first_negative([5, 7, -3, 10]))