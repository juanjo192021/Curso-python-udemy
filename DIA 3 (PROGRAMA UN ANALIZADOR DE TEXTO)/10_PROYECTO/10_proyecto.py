#Buenos días mis amigos como han amanecido los amo mucho , maricones
#Y para lograr esta parte , recuerda que hay un método de string que permite transformarlo en una lista
texto = input("Ingrese su texto : ").lower()
letras = []
letras.append(input("Ingrese su primera letra : ").lower())
letras.append(input("Ingrese su segunda letra : ").lower())
letras.append(input("Ingrese su tercera letra : ").lower())
print("\n")
print("CANTIDAD DE LETRAS")

resultado01 = texto.count(letras[0])
resultado02 = texto.count(letras[1])
resultado03 = texto.count(letras[2])
print(f"Se encontro la letra {letras[0]} repetida {resultado01} veces")
print(f"Se encontro la letra {letras[1]} repetida {resultado02} veces")
print(f"Se encontro la letra {letras[2]} repetida {resultado03} veces")

print("\n")
print("CANTIDAD DE PALABRAS")

resultado04 = texto.split()
print(f"Hemos encontrado {len(resultado04)} palabras en el texto")

print("\n")
print("PRIMERA Y ULTIMA PALABRA")

resultado05 = texto[0]
resultado06 = texto[-1]
print("La primera letra del texto es "+resultado05 +" y la última letra es " + resultado06)

print("\n")
print("PRIMERA Y ULTIMA PALABRA")

resultado04.reverse()
resultado07 = " ".join(resultado04)
print(f"El texto invertido es : \"{resultado07}\"")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")

buscarPython = "python" in texto
resultado08 = {True:'sí', False:'no'}
print(f"La palabra Python {resultado08[buscarPython]} se encuentra en el texto")
