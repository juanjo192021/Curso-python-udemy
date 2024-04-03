preciosCafe = [('capuchino',1.5),('expreso',2.2),('moka',1.9)]

def cafeMasCaro(listaPrecios):
    precioMayor=0
    cafeMasCaro = ''
    for cafe ,precio in listaPrecios:
        if precio > precioMayor:
            precioMayor = precio
            cafeMasCaro = cafe
        else:
            pass
    return cafeMasCaro,precioMayor

print(cafeMasCaro(preciosCafe))
cafe , precio = cafeMasCaro(preciosCafe)
print(f"El café más caro es {cafe} cuyo precio es {precio}")