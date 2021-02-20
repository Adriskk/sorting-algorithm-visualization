# => QUICK SORT ALGORITHM FILE

def partition(arr, low, high, change):
    i = (low - 1)  # index of smaller element
    pivot = arr[high].size_Y  # pivot

    for j in range(low, high):

        if arr[j].size_Y <= pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

            # => UPDATE A WINDOW
            change(arr[i], arr[j])

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # => UPDATE A WINDOW
    change(arr[i+1], arr[high])
    return i + 1


def quick_sort(elements, low, high, change):

    if len(elements) == 1:
        return elements

    if low < high:

        pi = partition(elements, low, high, change)

        quick_sort(elements, low, pi - 1, change)
        quick_sort(elements, pi + 1, high, change)

    return True
