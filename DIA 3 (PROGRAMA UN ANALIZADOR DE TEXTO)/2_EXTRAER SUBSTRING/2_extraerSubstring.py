texto  = "ABCDEFGHIJKLM"
#Cuenta desde el indice 2 hasta el indice menor a 5
fragmento01 = texto[2:5]
#Muestra desde el indice 2 hacia adelante
fragmento02 = texto[2:]
#Muestra desde los indices menos a 5
fragmento03 = texto[:5]
#Muestra los indices comprendidos entre 2 y 9, pero con un salto linea de 2 indices
fragmento04 = texto[2:10:3]
#Muestra todos los indices pero con un salto de linea de 2 espacios
fragmento05 = texto[::3]
#Muestra la cadena invertida
fragmento06 = texto[::-1]
#Muetra la cadena invertida pero con un saldo de linea de 1 espacio
fragmento07 = texto[::-2]
print(fragmento01)
print(fragmento02)
print(fragmento03)
print(fragmento04)
print(fragmento05)
print(fragmento06)
print(fragmento07)

