# Ejemplo exportar fichero con formato .xlsx
# Primero instalamos openpyxl para poder utilizar las funcionalidades para excel con
# pip install openpyxl

import pandas as pd

# leer_fichero = pd.read_csv(r'catalogo_cf_10.csv')
# leer_fichero.to_excel(r'catalogo_cf_10.xlsx', index=None, header=True)

# # Este es el que ha funcionado
# leer_fichero = pd.read_csv(r'catalogo_cf.csv', encoding="ISO-8859-1")
# leer_fichero.to_excel(r'catalogo_cf.xlsx', index=None, header=True)

# #
# # Probando con otros encodings porque salen mal los acentos
# # leer_fichero = pd.read_csv(r'catalogo_cf_10.csv', encoding="ISO-8859-1")
# # leer_fichero.to_excel(r'catalogo_cf_10_encoding.xlsx', index=None, header=True)
# #
# # leer_fichero = pd.read_csv(r'catalogo_cf_10.csv', encoding="UTF-8")
# # leer_fichero.to_excel(r'catalogo_cf_10_encoding_UTF-8.xlsx', index=None, header=True)
# #
# # leer_fichero = pd.read_csv(r'catalogo_cf_10.csv', encoding="windows-1252")
# # leer_fichero.to_excel(r'catalogo_cf_10_encoding_windows-1252.xlsx', index=None, header=True)

# Se crea el dataframe con pandas de un fichero Excel
dataframe_excel = pd.read_excel("catalogo_cf.xlsx")
print(dataframe_excel)

# Selecciona la primera y la cuarta columna
print(dataframe_excel.iloc[:, [0, 3]])

# Se exporta a Excel
dataframe_excel.iloc[:, [0, 3]].to_excel('catalogo_cf_resumen.xlsx')
