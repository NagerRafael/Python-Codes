#Discretización  de la función Fuerza vs Tiempo
def Fuerza(tiempo):
    tuplas = [(0.0,0.0),(0.01,14),(0.03,40)] #Se requiere discretizar la función observando su gráfica.
    #U obteniendo pares coordenados de la función.
    #tiempos = [t[0] for t in tuplas]
    #fuerzas = [f[1] for f in tuplas]

    t0=tiempo
    tup2 = [t for t in tuplas if (t[0]>t0)][0]
    tup1 = tuplas[tuplas.index(tup2)-1 if tuplas.index(tup2)!= 0 else 0]
    
    #Función de Interpolación
    # y = [(y2 - y1)/(x2 - x1)]*(x0 - x1) + y1
    t2,f2 = tup2
    t1,f1 = tup1

    return (f2-f1)/(t2-t1)*(t0-t1)+f1
print(Fuerza(0.025))
