palabra = 'python'

lista = [letra for letra in palabra]
print(lista)

lista01 = [n/2 for n in range(0,21,2)]
print(lista01)

lista02 = [n for n in range(0,21,2) if n*2 > 10]
print(lista02)

lista03 = [n if n*2 > 10 else 'no' for n in range(0,21,2)]
print(lista03)

pies = [10,20,30,40,50]
metros = [m/3.281 for m in pies]
print(metros)