# Ejemplo para leer un fichero

# # Lee el fichero completo
# fichero = open("quijote_pg2000.txt", 'r')
# for linea in fichero:
#     print(linea)
# fichero.close()
# Deja una línea en blanco entre cada línea

# # Lee el fichero completo <-- Tampoco funciona este fichero
# fichero = open("quijote_pg2000_UTF-8.txt", 'r')
# for linea in fichero:
#     print(linea)
# fichero.close()
# # Deja una línea en blanco entre cada línea

# # Lee los 200 primeros caracteres de un fichero
# with open("quijote_pg2000.txt", 'r') as fichero:
#     contenido = fichero.read(200)
#     print(contenido)

# # Quiero leer solo la primera línea
# with open("quijote_pg2000.txt", 'r') as file:
#     contenido = file.readline()
#     print(contenido)

# # Lee los párrafos de un fichero
# # strip() evita una línea en blanco entre ellos
# with open("quijote_pg2000.txt", 'r') as file:
#     contenidos = file.readlines(2000)
#     for c in contenidos:
#         print(c.strip())

# # Ahora vamos a crear un fichero nuevo:
# entrada = """Primera parte del ingenioso hidalgo don Quijote de la Mancha
#
#
# """
#
# # Creamos un fichero y pegamos el texto de la variable entrada
# with open("quijote-ext01.txt", 'x') as file:
#     file.write(entrada)

# # Vamos a hacer un append:
# entrada_agregar = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
# no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua,
# rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, ...
#
# """
# # Abrimos el fichero y adjuntamos el texto de la variable entrada_agregar
# with open("quijote-ext01.txt", 'a') as file:
#     file.write(entrada_agregar)

# Busca a partir del carácter 18 e imprime los 42 caracteres siguientes
with open("quijote-ext01.txt", 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)
