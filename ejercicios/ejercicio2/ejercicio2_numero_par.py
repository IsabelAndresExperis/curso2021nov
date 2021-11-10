# Ejercicio 2:
#     Preguntar al usuario un número y mostrar si es par o impar.
#     Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario.

def pedir_numero():
    numero = input("Escriba un número: ")
    if (int(numero) % 2) == 0:
        if (int(numero) % 4) == 0:
            print(f"El número {numero} es par y múltiplo de cuatro")
        else:
            print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")


pedir_numero()

# Hago la compilación a bytecode y funciona

# Hago la compilación a ejecutable y funciona
