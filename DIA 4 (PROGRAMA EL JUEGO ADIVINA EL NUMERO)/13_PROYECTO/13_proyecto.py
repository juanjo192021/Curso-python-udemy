from random import randint
nombre = input("¿Cuál es su nombre?: ")
random = randint(1,100)
intentos = 0
while intentos<8:
    numero = int(input(f"{nombre}, ingrese un numero entre el 1 y el 100 ({8-intentos} restantes): "))
    if random > numero > 0 and numero<100:
        print("El número ingresado es menor")
        intentos +=1
    elif numero>random and 100 > numero > 0:
        print("El número ingresado es mayor")
        intentos += 1
    elif numero == random:
        print(f"Felicidades {nombre}, ganaste utilizando {intentos} intentos")
        break
    else:
        print("El número ingresado es menor o mayor al rango permitido")
        intentos += 1
else:print("Fin del juego")