"""
Los string son inmutables, no pueden cambiarse su contenido o su orden
nombre = "Carina"
nombre[0] = "K"
"""
#Aqui cambiamos el contenido de las variables, pero no el contenido del string principal

nombre = "Carina"
nombre = "Karina"
print(nombre)

# Multiplicar string

n1 = "Kari"
print(n1*10)

#Hace un salto de lineas en un string con solamente comillas

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

#Imprime si agua existe en poema, devuelve boolean

print("agua" not in poema)

#Saber el largo de un string, o sea la cantidad de caracteres

texto = "Hola mundo"
print(len(texto))