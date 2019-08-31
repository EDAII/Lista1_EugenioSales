def binary_search(key, array):

    counter = 0
    lim_inf = 0
    lim_sup = len(array) - 1
    
    while(lim_inf <= lim_sup):
        mid = (lim_inf+lim_sup)//2
        counter += 1
        if array[mid] == key:
            return counter
        elif array[mid] > key:
            lim_sup = mid - 1
        else:
            lim_inf = mid + 1
        
            
    return (-1)
        