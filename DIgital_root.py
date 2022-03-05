def digital_root(n):
    r = n
    while r > 9:    #Mientras el resultado tenga decimales...
        n_list = list(map(lambda x: int(x), (m for m in str(r)))) #Covierte el int en str, lo itera evaluandolo en la función lambda y termina convirtiendo de map a list.
        r = 0       #Se prepara para el acumulador
        for x in n_list:     #Iteración de los dígitos del número
            r += x          #Suma acumulada de todos los dígitos
    return r        #Retorno del resultado