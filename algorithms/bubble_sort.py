# => BUBBLE SORT ALGORITHM FILE

def bubble_sort(elements, change):

    for i in range(len(elements)):

        for j in range(len(elements)-1):

            if elements[j].size_Y > elements[j+1].size_Y:

                # => SWAP
                elements[j], elements[j+1] = elements[j+1], elements[j]

                # => UPDATE A WINDOW
                change(elements[j], elements[j+1])
    return True
