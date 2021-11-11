# Importar todo un módulo:
# import math

# raiz_cuadrada = math.sqrt(10)
# logaritmo_base10 = 20 * math.log10(2)
# print(raiz_cuadrada)
# print(logaritmo_base10)

# # Importar una parte de un módulo o sólo algunas funciones:
# from math import sqrt, log10
#
# # En este caso hay que quitar math. de delante de las funciones
# raiz_cuadrada = sqrt(10)
# logaritmo_base10 = 20 * log10(2)
# print(raiz_cuadrada)
# print(logaritmo_base10)

# Otra manera de importar, creando un objeto al que luego hacemos referncia
import math
# # Para este módulo no es necesario, funciona sin esto,
# # pero para nuestros módulos o módulos de terceros sí sería necesario
# math

print(math.log10(5))
print(math.pi)

# import calcular_media
# calcular_media.calcular_media(3, 5, 7)
