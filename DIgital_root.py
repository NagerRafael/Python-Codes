def digital_root(n):
    r = n
    while r > 9:    #Mientras el resultado tenga decimales...
        n_list = list(map(lambda x: int(x), (m for m in str(r)))) #Covierte el int en str, lo itera evaluandolo en la función lambda y termina convirtiendo de map a list.
        r = sum(n_list) #Suma de todos los dígitos del número
    print(r)
    return r        #Retorno del resultado