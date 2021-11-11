# Ejercicio 3:
#     Escribir un programa que tome una lista de números (entre 5 y 10 números),
#     haga una lista con el primero y el último de los elementos,
#     otra con el valor máximo y mínimo,
#     y por último las muestre en pantalla.

def pedir_lista():
    min_numeros = 5
    max_numeros = 10

    lista_numeros = []
    for i in range(0, min_numeros):
        numero_actual = input(f"Introduzca un número ({i + 1}º): ")
        lista_numeros.append(int(numero_actual))

    for i in range(min_numeros, max_numeros):
        numero_actual = input(f"Introduzca un número ({i + 1}º) (o s para terminar lista): ")
        if numero_actual == 's':
            break
        else:
            lista_numeros.append(int(numero_actual))

    print(f"Esta es la lista de números introducidos: {lista_numeros}")
    lista_primero_ultimo = [lista_numeros[0], lista_numeros[-1]]
    print(f"El primer número introducido es el {lista_primero_ultimo[0]} y el último el {lista_primero_ultimo[1]}")
    lista_numeros.sort()
    lista_max_min = [lista_numeros[-1], lista_numeros[0]]
    print(f"El número máximo introducido es el {lista_max_min[0]} y el número mínimo el {lista_max_min[1]}")


pedir_lista()
