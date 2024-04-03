nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]

combinados = list(zip(nombres,edades))
print(combinados)

#Predomina el menor número del índice de ambas listas

nombres01 = ['Ana','Hugo','Valeria']
edades01 = [65,29,42,45]

combinados = list(zip(nombres01,edades01))
print(combinados)

#
nombres02 = ['Ana','Hugo','Valeria']
edades02 = [65,29,42]
ciudades02 = ['Lima','Madrid','Mexico']
combinados = list(zip(nombres02,edades02,ciudades02))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")