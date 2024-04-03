cliente = {'nombre': 'Juan Jose',
           'edad':45,
           'ocupacion':'instructor'}

pelicula = {'titulo':'Matrix',
            'fichaTecnica':{'protagonista':'Keanu Reeves',
                            'director':'Lana y Lilly Wachowski'}}
elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case{'nombre': nombre,
             'edad':edad,
             'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case{'titulo':titulo,
             'fichaTecnica':{'protagonista':protagonista,
                            'director':director}}:
             print("Es una pelicula")
             print(titulo,protagonista,director)
        case _:
            print("No sé que es esto")
