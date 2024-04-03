#Las claves(c1) no se pueden repetir, mientras los valores pueden repetirse(valor1)
diccionario = {'c1':'valor1','c2':'valor2'}
#Obtiene el valor por medio de su llave
resultado01 = diccionario['c2']
cliente = {'nombre':'Juan', 'apellido':'Pérez', 'peso':88, 'talla': 1.76}
consulta = cliente['apellido']
dic = {'c1': 55,'c2': [10,20,30],'c3':{'s1':100, 's2':200}}
resultado02 = dic['c2'][2]
resultado03 = dic['c3']['s2']
#Agregar elementos a un diccionario
diccionario02 = {1:'a',2:'b'}
diccionario02[3]='c'
#Sobreescribir un elemento existente
diccionario02[2]='B'
#Saber todas las claves de los diccionarios
print(cliente.keys())
#Saber todos los valores de los diccionarios
print(cliente.values())
#Saber que hay dentros de los diccionarios
print(cliente.items())
print(diccionario02)
print(type(diccionario))
print(resultado01)
print(consulta)
print(resultado02)
print(resultado03)
print(diccionario02)