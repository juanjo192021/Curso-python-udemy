#from random import randint
from random import *
from random import choice

#Aleatorios enteros
aleatorio01 = randint(1,20)
print(aleatorio01)

#Aleatorios flotantes
aleatorio02 = uniform(1,3)
print(aleatorio02)

#Aleatorios flotantes entre 0 y 1
aleatorio03 = random()
print(aleatorio03)

#Aleatorios en string

colores = ['azul','rojo','verde','amarillo']
aleatorio04 = choice(colores)
print(aleatorio04)

# Desordena el orden aleatoriamente

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)


