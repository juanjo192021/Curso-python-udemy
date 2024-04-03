mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista4 = ["g","o","b","m","c"]
mi_lista5 = ["g","o","b","m","c"]
#Saber el largo de una lista
resultado01 = len(mi_lista)
#Extraer el valor de una lista mediante su indice
resultado02 = mi_lista[0]
#Imprime la lista desde un rango inicia hasta un rango final mi_lista[desde el indice que inicia : hasta el indice que se desea + 1]
resultado03 = mi_lista[0:2]
#Alterar sus elementos
mi_lista3[0] = "Alfa"
#Agregar elementos
mi_lista3.append("g")
#Eliminar elementos .pop(El indice que se desea eliminar) y tambien se puede almacenar en un variable
resultado04 = mi_lista3.pop(0)
#Ordenan alfabeticamente tanto como letras y numeros
mi_lista4.sort()
#Invierte el orden de la lista, pero no las ordena
mi_lista5.reverse()
print(type(mi_lista))
print(resultado01)
print(resultado02)
print(resultado03)
print(mi_lista3)
print(resultado04)
print(mi_lista4)
print(mi_lista5)
