monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo más monedas")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir ?(s/n) :  ")
else:
    print("Gracias")

respuesta01 = 's'
while respuesta01 == 's':
    #Reserva un espacio para el programador
    pass
print("hola")

nombre = input("Tu nombre : ")

for letra in nombre:
    # Omite los caracteres que están después de que coincida con la condicion
    if letra == 'r':

        break
    print(letra)

nombre02 = input("Tu nombre : ")
for letra in nombre:
    # Omite el caracter con el que coincide en el if
    if letra == 'r':
        continue
    print(letra)