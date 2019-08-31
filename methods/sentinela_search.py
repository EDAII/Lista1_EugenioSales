def sentinela_search(key, array):
    size = len(array)
    array.append(key)
    i = 0
    while(key != array[i]):
        i+=1
    if i < size:
        return i
    return (-1)
