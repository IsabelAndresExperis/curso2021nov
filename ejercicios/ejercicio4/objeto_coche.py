# Ejercicio 4: CLASE COCHE
#     Modificar el código de la clase coche para que pueda ser llamado desde un nuevo fichero.
#     1.- El fichero de la clase se debe llamar clase_coche.py
#     2.- El Fichero del objeto desde donde llamar a la clase: objeto_coche.py
#     3.- Crear al menos una instancia para llamar al objeto y a la clase

import clase_coche


def instanciar_coche(p_marca, p_modelo, p_tipo):
    if p_tipo == 'C':
        return clase_coche.Coche(p_marca, p_modelo, 'Combustión')
    elif p_tipo == 'E':
        return clase_coche.CocheElectrico(p_marca, p_modelo, 'Eléctrico')
    else:
        return


def comprar_coche():
    comprar = input("¿Quieres comprarte un coche? (S/N) ")
    if comprar == 'S':
        input_marca = input("¿De qué marca? ")
        input_modelo = input("¿De qué modelo? ")
        input_tipo = input("¿De qué tipo? Escribe 'C' si lo quieres de combustión o 'E' si lo quieres eléctrico: ")
        return instanciar_coche(input_marca, input_modelo, input_tipo)
    elif comprar == 'N':
        print("¡¡¡ Pues era gratis !!!")
        return
    else:
        print("No he entendido tu respuesta")
        return


def arrancar():
    tienes_coche = input("¿Tienes coche? (S/N) ")
    if tienes_coche == 'S':
        input_marca = input("¿De qué marca? ")
        input_modelo = input("¿Qué modelo es? ")
        input_tipo = input("¿De qué clase es? Escribe 'C' si es de combustión o 'E' si es eléctrico: ")
        return instanciar_coche(input_marca, input_modelo, input_tipo)
    elif tienes_coche == 'N':
        return comprar_coche()
    else:
        print("No he entendido tu respuesta")
        return


def conducir_coche(coche):
    if type(coche) == clase_coche.Coche:
        if coche.nivel_gasolina == 0:
            repostar = input("El coche está sin combustible, ¿quieres repostar? (S/N) ")
            if repostar == "S":
                coche.gasolina_completo()
                coche.conducir()
            elif repostar == "N":
                print("¡El coche no arranca porque no tiene combustible!")
            else:
                print("No he entendido tu respuesta")
        else:
            coche.conducir()
    elif type(coche) == clase_coche.CocheElectrico:
        if coche.nivel_carga == 0:
            recargar = input("El coche está sin batería, ¿quieres cargarlo? (S/N) ")
            if recargar == "S":
                coche.cargar()
                coche.conducir()
            elif recargar == "N":
                print("¡El coche no arranca porque la batería está agotada!")
            else:
                print("No he entendido tu respuesta")
        else:
            coche.conducir()
    else:
        print("No se conducir tu coche")


coche_usuario = arrancar()
if coche_usuario is None:
    print("No tienes coche, no puedes conducir")
else:
    quiere_conducir = input(f"Tienes este coche: {coche_usuario.marca} {coche_usuario.modelo} ({coche_usuario.tipo})\n"
                            f"¿Quieres conducir? (S/N) ")
    if quiere_conducir == "S":
        conducir_coche(coche_usuario)
    elif quiere_conducir == "N":
        print("¿Entonces para qué quieres el coche?")
    else:
        print("No he entendido tu respuesta")
