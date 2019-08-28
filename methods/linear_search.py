def linear_search(array, value):
    counter = 0
    for i in array:
        counter += 1
        if value == i:
            return counter

    return counter