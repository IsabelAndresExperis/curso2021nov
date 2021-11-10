# Ejemplo uso de la librería fnmatch
import fnmatch
import os

# Busca todos los ficheros con el patrón especificado
patron = 'ejemplo*.py'
print('Patrón: ', patron)
print('*****')

ficheros = os.listdir('./')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))

print('Nombre: ', ficheros)
print('Coinciden: ', fnmatch.filter(ficheros, patron))
