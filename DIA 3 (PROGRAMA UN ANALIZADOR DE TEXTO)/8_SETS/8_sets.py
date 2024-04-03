mi_set = set({1,2,3,4,5,1,1,1,2,2,2})
print(type(mi_set))
#Los sets descartan los numeros repetidos automaticamente
print(mi_set)
#Se puede agregar solamente tuples, no se le puede agregar listas o diccionarios, ya que no cumplen el criterio de inmutabilidad que desea los sets
mi_set2 = set({1,2,3,4,5,(7,8,9)})
print(mi_set2)
#Saber la cantidad de elementos
print(len(mi_set2))
#Saber si un elemento esta en una lista, diccionario, tuple o sets
print(2 in mi_set2)
#Union de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
#Agregar un elemento
s4 = {1,2,3}
s4.add(9)
print(s4)
#Eliminar un elemento y de no encontrarlo da un error
s5 = {1,2,3}
s5.remove(2)
print(s5)
#Descarta un elemento y de no encontrarlo sigue con la lista
s6 = {1,2,3}
s6.discard(9)
print(s6)
#Elimina un elemento aleatorio
s7 = {1,2,3}
s7.discard(9)
print(s7)
#Limpiar los elementos del set
s8 = {1,2,3}
s8.clear()
print(s8)
"""
#Es lo mismo que lo que esta en la parte inferior
otro_set = {1,2,3}
print(otro_set)

#Los objetos sets no pueden ser suscriptibles

ej : otro_set[0] = 15

"""