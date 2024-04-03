mi_tuple = (1,2,3,4)
mi_tuple02 = (1,2,(10,20),4)
mi_tuple03 = (1,2,3,4)
mi_tuple04 = (1,2,3,1)
"""
Los tuples son objetos que no soportan asignaciones de items
mi_tuple[0]= 5
"""
#Casting
mi_tuple03 = list(mi_tuple03)
#Asignar valores de los tuples a variables deben tener la misma cantidad de valores y variables
x,y,z,a = mi_tuple04
print(type(mi_tuple))
print(mi_tuple[-2])
print(mi_tuple02[2][0])
print(type(mi_tuple03))
print(x,y,z,a)
#Cantidad de elementos de un tuple
print(len(mi_tuple04))
#Cuenta la cantidad de veces que se repite el número dentro del parentesis
print(mi_tuple04.count(1))
#Permite saber el índice del valor que está dentro del parentesis
print(mi_tuple04.index(2))

