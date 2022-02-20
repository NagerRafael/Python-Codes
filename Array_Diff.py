def array_diff(a, b):
    set_b = set(b)  #Crea un conjunto donde se ignoran los elementos repetidos
    return [i for i in a if i not in set_b] #Se devuelven los valores que no están en el conjunto b