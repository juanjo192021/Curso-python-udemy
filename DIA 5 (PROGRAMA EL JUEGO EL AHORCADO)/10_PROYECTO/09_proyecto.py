from random import *
palabras= ['pito','casa','campo','sumadi','maincrafita']
letrasCorrectas = []
letrasIncorrectas = []
intentos = 6
aciertos = 0
juegoTerminado = False

def elegirLetra(listaPalabras):
    palabraElegida = choice(listaPalabras)
    letrasUnicas = len(set(palabraElegida))
    print(set(palabraElegida))
    return palabraElegida,letrasUnicas

def pedirLetra():
    letraElegida = ''
    esValida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not esValida:
        letraElegida = input(f"Ingresa una letra: ").lower()
        if letraElegida in abecedario and len(letraElegida)==1 :
            esValida = True
        else:
            print('No has elegido una letra correcta')
    return letraElegida
def mostraNuevoTablero(palabraElegida):
    listaOculta=[]
    for l in palabraElegida:
        if l in letrasCorrectas:
            listaOculta.append(l)
        else:
            listaOculta.append('-')
    print(' '.join(listaOculta))
def chequearLetra(letraElegida, palabraOculta, vidas, coincidencias):

    fin = False
    if letraElegida in palabraOculta:
        letrasCorrectas.append(letraElegida)
        coincidencias +=1
    else:
        letrasIncorrectas.append(letraElegida)
        vidas -=1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letraUnicas:
        fin = ganar(palabraOculta)
    return  vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print(f"La palabra oculta era {palabra}")
    return  True
def ganar(palabraDescubierta):
    mostraNuevoTablero(palabraDescubierta)
    print("Felicitaciones has encontrado la palabra !!!")
    return True



palabra, letraUnicas = elegirLetra(palabras)

while not juegoTerminado:
    print('\n' + '*'*20 + '\n')
    mostraNuevoTablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letrasIncorrectas))
    print(f'Vidas : {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedirLetra()
    intentos, terminado, aciertos = chequearLetra(letra, palabra, intentos, aciertos)
    juegoTerminado = terminado