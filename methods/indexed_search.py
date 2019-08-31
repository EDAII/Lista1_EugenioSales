def table_index(index):
    size = len(index)
    slots = size // 10
    i = 0
    
    table = []
    table.append(i)
    while i < size:
        i+=slots
        table.append(i-1)

    return table

def indexed_search(key, array):
    index = table_index(array)
    counter = 0
    
    for i in index:
        if key > i:
            lim_inf = i
        elif key < i:
            lim_sup = i
        else:
            break
    
    for i in range(lim_inf, lim_sup):
        counter+=1
        if key == i:
            return counter
    
    return (-1)

        
            
    