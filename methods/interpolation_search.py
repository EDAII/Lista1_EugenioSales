def interpolation_search(key, array):
    lim_inf = 0
    lim_sup = len(array) - 1
    
    counter = 0
    
    while lim_inf < lim_sup:
        
        counter+=1
        
        mid = lim_inf + ((lim_sup - lim_inf) * ((key - array[lim_inf]) // (array[lim_sup] - array[lim_inf])))
        print(mid)
        
        
        if key == array[mid]:
            return counter
        elif key > array[mid]:
            lim_inf = mid + 1
        else:
            lim_sup = mid - 1
        
        return (-1)
    