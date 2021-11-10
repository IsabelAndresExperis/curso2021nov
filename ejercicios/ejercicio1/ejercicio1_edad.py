# Ejercicio 1:
#     Crear un programa que le pregunte al usuario su nombre y edad
#     y le muestre el año en que cumplirá los 100 años
import datetime


def preguntar():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuál es tu edad? "))
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    ano100 = datetime.datetime.now().year + 100 - edad

    print(f"Hola {nombre}, cumplirás 100 años en el año {ano100}")


preguntar()

# Compilando a bytecode:
# Ir a la terminal y ejecutar los siguientes comandos:
# # Averiguo dónde está el fichero que quiero compilar a bytecode y voy allí antes de ejecutar Python:
# dir
# cd ejercicios
# dir
# cd ejercicio1
# # Entro en Python:
# python
# # Importo el py_compile y compilo el fichero .py:
# >>>import py_compile
# >>>py_compile.compile("ejercicio1_edad.py")
# # Esto genera el fichero:
# '__pycache__\\ejercicio1_edad.cpython-310.pyc'
#
# # Salgo del Python porque la ejecución del bytecode se hace desde fuera:
# >>>quit()
# # Ejecución del bytecode generado:
# python __pycache__\\ejercicio1_edad.cpython-310.pyc

# Compilando a ejecutable del sistema:
# # Ya tengo instalado pyinstaler, que me permite hacer esta compilación
# # Ya estoy situada en el directorio donde está el archivo que quiero compilar
# # Desde fuera de Python, en la terminal escribo:
# pyinstaller --onefile ejercicio1_edad.py
# # Se generan las carpetas build y dist.
# # En la carpeta dist están todas las librerías necesarias para su distribución

# # NOTA: Instalación del pycompiler en Windows:
# # Ejecutar en el terminal:
# pyp install pyinstaller
