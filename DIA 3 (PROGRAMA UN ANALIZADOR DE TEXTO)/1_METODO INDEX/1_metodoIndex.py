miTexto = "Esta es una prueba"
resultado = miTexto[9]
print(resultado)
resultado01 = miTexto[-4]
print(resultado01)
resultado02 = miTexto.index("n")
print(resultado02)
resultado03 = miTexto.index("prueba")
print(resultado03)
#desde la posicion 5 hasta la posicion 16 -1
resultado04 = miTexto.index("a",5, 16)
print(resultado04)
#busca desde el ultimo al primero
resultado05 = miTexto.rindex("a")
print(resultado05)