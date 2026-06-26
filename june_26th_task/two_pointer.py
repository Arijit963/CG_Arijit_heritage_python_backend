def pair_sum(arr, target):

    left = 0
    right = len(arr)-1

    while left < right:

        current = arr[left] + arr[right]

        if current == target:
            return True

        elif current < target:
            left += 1

        else:
            right -= 1

    return False

arr = [1,2,3,4,5,6,7,8]
print(pair_sum(arr,10))
