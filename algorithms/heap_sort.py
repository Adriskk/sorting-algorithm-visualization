# => HEAP SORT ALGORITHM FILE

def heapify(arr, n, i, change):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest].size_Y < arr[l].size_Y:
        largest = l

    if r < n and arr[largest].size_Y < arr[r].size_Y:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # => UPDATE A WINDOW
        change(arr[i], arr[largest])

        heapify(arr, n, largest, change)


def heap_sort(elements, change):
    n = len(elements)

    for i in range(n // 2 - 1, -1, -1):
        heapify(elements, n, i, change)

    for i in range(n - 1, 0, -1):
        elements[i], elements[0] = elements[0], elements[i]

        # => UPDATE A WINDOW
        change(elements[i], elements[0])

        heapify(elements, i, 0, change)

    return True
