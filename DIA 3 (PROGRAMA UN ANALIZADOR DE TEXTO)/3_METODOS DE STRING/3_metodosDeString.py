texto01 = "Este es el texto de Juan"
#Convierte los caracteres en mayuscula
resultado01 = texto01.upper()
#Convierte los caracteres en minuscula
resultado02 = texto01.lower()
#Separa el texto en una lista
resultado03 = texto01.split()
#Separa el texto en una lista con un caracter ingresado
resultado04 = texto01.split("t")

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
#Incluye los elementos dentro del parentesis y las separa con un espacio entre cada uno de ellos
resultado05= " ".join([a,b,c,d])
#La diferencia entre el .index y el .find es que el find no arroja un error cuando no se encuentra el valor, ya que arroja -1
resultado06 = texto01.index("l")
resultado07 = texto01.find("t")
#Sirve para reemplar un fragmento de un texto .replace(antiguo, nuevo, cuanto antiguos deseas cambiar)
resultado08 = texto01.replace("e","x",1)
print(resultado01)
print(resultado02)
print(resultado03)
print(resultado04)
print(resultado05)
print(resultado06)
print(resultado07)
print(resultado08)