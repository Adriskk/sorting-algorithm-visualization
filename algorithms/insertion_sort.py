# => INSERTION SORT ALGORITHM FILE

def insertion_sort(elements, change):

    for i in range(1, len(elements)):

        key = elements[i]

        j = i - 1
        while j >= 0 and key.size_Y < elements[j].size_Y:
            elements[j + 1], elements[j] = elements[j], elements[j + 1]

            # => UPDATE A WINDOW
            change(elements[j + 1], elements[j])

            j -= 1

        elements[j + 1].size_Y = key.size_Y

    return True


