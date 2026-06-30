def quick_sort(arr, low=0, high=None):

    if high is None:
        high = len(arr) - 1

    if low < high:

        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)

        quick_sort(arr, pivot_index + 1, high)

    return arr

def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

delivery_minutes = [45, 12, 30, 8, 52, 25, 18, 40]

quick_sort(delivery_minutes)

print(delivery_minutes)

print("Next Delivery:", delivery_minutes[0])