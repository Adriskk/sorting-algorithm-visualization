# => SELECTION SORT ALGORITHM FILE

def selection_sort(elements, change):
    for i in range(len(elements)):

        min_index = i

        for j in range(i + 1, len(elements)):

            if elements[min_index].size_Y > elements[j].size_Y: min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

        # => UPDATE A WINDOW
        change(elements[min_index], elements[i])

    return True
