def array_diff(a, b):
    for x in b:         #Iterating the elements has removed
        while x in a:   #While element x is in the list a
            a.remove(x) #Remove element x from list a
    return a