# Ejemplo de función lambda
# Con una función normal sería:
def multiplicar(x, y):
    return x * y


print(multiplicar(5, 5))

# Con una función lambda:
multiplicar_lambda = lambda x, y: x * y
print(multiplicar_lambda(5, 8))

# Con más funcionalidad
imprimir_multiplicacion = lambda x, y: print(str(x * y))
imprimir_multiplicacion(7, 5)
