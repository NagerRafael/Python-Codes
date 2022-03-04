def anagrams(word, words):
    result = []             #Lista resultante ha retornar
    def Character(word):    #Función, devuelve un diccionario con cada letra única y su cantidad.
        dicc = {}                               #Define un diccionario vacio
        for char in word:                       #Recoriendo en cada caracter de la palabra
            if char not in dicc.keys():         #Condicional para evitar repetidos
                dicc[char] = word.count(char)   #Agrega la clave caracter y el valor cantidades presentes.
        return dicc                             #Retorno de diccionario
    dic_word = Character(word);     #Diccionario de la palabra principal
    
    for x in words:             #Recoriendo cada palabra de la lista
        dic_x = Character(x);   #Creando un diccionario de caracteres
        if dic_word == dic_x:   #Comparando si ambos diccionarios son iguales
            result.append(x)    #Agregar a la lista final las palabras que sean anagramas
    return result               #Salida
    