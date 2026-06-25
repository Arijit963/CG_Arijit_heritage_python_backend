def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr

student_marks = [78, 55, 92, 43, 88, 67, 100, 35]

sorted_marks = bubble_sort(student_marks.copy())

print("Sorted marks:", sorted_marks)