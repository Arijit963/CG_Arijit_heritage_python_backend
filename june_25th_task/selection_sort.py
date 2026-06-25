def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

item_prices = [299, 150, 499, 75, 350, 225, 125]

sorted_prices = selection_sort(item_prices.copy())

print("Prices:", sorted_prices)

print("3 Cheapest:", sorted_prices[:3])