def linear_search (list, val):
    for index, v in enumerate(list):
        if v == val:
            return index
    else :
        return None
    
