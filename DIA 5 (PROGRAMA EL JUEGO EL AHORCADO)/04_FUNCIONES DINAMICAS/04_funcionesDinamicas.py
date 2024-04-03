def chequear3Cifras(lista):
    lista3Cifras =[]
    for n in lista:
        if n in range(100,1000):
            lista3Cifras.append(n)
        else:
            pass
    return lista3Cifras
resultado = chequear3Cifras([550,99,600])
print(resultado)