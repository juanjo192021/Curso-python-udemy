def suma_menores(lista):
    suma =0
    for elemento in lista:
        if 1000>elemento>0:
            suma += elemento
        else:
            pass
    return suma
lista_numeros = [500,600,-55]