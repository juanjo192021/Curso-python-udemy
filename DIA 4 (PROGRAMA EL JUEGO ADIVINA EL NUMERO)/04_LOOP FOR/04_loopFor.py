lista = ['a','b','c','d']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    #print("Letra: " + letra)
    print(f"Letra {numero_letra} : {letra}")

lista02 = ['pablo', 'laura', 'fede','luis','julia']
for nombre in lista02:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no se encontraron con L")

numeros = [1,2,3,4,5]
miValor = 0

for numero in numeros:
    miValor += numero
print(miValor)

for a, b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for item in dic.keys():
    print(item)