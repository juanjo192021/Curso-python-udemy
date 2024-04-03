lista = ['a','b','c']

for indice, item in enumerate(lista):
    print(indice, item)

lista2 = ['a','b','c']

misTuples = list(enumerate(lista))
print(misTuples)
print(misTuples[1][0])