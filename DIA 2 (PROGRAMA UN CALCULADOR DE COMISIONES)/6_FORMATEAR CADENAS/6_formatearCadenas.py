from locale import str

x = 10
y = 5
color = "rojo"
matricula = 541926

print("Mis numeros son " + str(x) + " y "+ str(y))
print("Mis numeros son  {} y {}".format(x,y))
print("La suma de {} y {} es {}".format(y,x, x+y))
print(f"El auto es {color} y su matricula es {matricula}")