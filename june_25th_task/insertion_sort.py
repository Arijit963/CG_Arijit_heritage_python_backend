def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr

hr_employee_ids = [1001, 1003, 1007, 1012, 1020]

new_employee = 1008

hr_employee_ids.append(new_employee)

sorted_ids = insertion_sort(hr_employee_ids)

print(sorted_ids)