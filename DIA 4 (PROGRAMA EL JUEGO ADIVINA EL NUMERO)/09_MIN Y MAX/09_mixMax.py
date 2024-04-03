menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

lista = [58,96,72,64,35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['juan','pablo','alicia','carlos']
print(min(nombres))

#Empieza a leer desde las mayusculas,
#La solucion seria print(min(nombre.lower()))
nombre = 'Carlos'
print(min(nombre))

dic = {'c1': 45, 'c2':11}

print(min(dic))
print(min(dic.values()))