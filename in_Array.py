def in_array(array1, array2):
    result = []
    for a2 in array2:
        for a2 in array1:
            if a2.find(a1) and a1 not in array2:
                result.append(a1)
    result.sort()
    return result