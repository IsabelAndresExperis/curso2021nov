# Ejemplo para expresiones regulares
import re

texto = "Hoy es un día magnífico y maravilloso"
exp_reg = re.search("^Hoy", texto)
print(exp_reg)

expr_reg_ = re.search("^Hoy.*", texto)
print(expr_reg_)

expr_reg2 = re.findall("ma", texto)
print(expr_reg2)

exp_reg3 = re.sub("\\s", "    ", texto)
print(exp_reg3)
