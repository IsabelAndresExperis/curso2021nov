#
import os
import shutil


# # Copiar ficheros situados en el mismo directorio
# shutil.copy(src="quijote-ext01.txt", dst="quijote-ext02.txt")
#
# # Copiar ficheros preservando los metadatos
# shutil.copy2(src="quijote-ext01.txt", dst="quijote-ext04.txt")

# # Copiar al igual que el comando cp -R en GNU/Linux
# shutil.copytree(src="../clase3/", dst="../clase3copia")
#
# # Ignorar ficheros .jpg al copiar
# shutil.copytree(src='../clase3/', dst="../clase3copia_ignorar/", ignore=shutil.ignore_patterns('*lambda*'))

# Mover (o cambiar de nombre al fichero) al igual que el comando mv en GNU/Linux
shutil.move(src="../main.py", dst="../clase3copia/main_copia.py")
# Para restituirlo en su sito original:
# shutil.move(src="../clase3copia/main_copia.py", dst="../main.py")

# # Lo siguiente con la librería os no ha funcionado, están mal las rutas y nombres:
# # Mover un fichero usando la biblioteca os
# os.rename("../imagen.jpg", "directorio1/imagen.jpg")
#
# # Borrar un fichero
os.remove("directorio1/imagen.jpg")
