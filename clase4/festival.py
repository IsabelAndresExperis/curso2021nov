# import datetime

class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # inicializa los parámetros
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    @classmethod
    def valor_ticket(cls, valor):
        # Este atributo aparece aquí por primera vez y aquí se define
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


# Se crea una instancia de la clase Festival Musical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')

# Se accede a los atributos del objeto
print(festival1.nombre)

# Muestra la posición del objeto de la clase FestivalMusical en la memoria
print(festival1)

# Otros accesos
print(festival1.nombre.upper())

festival2 = FestivalMusical('Primavera sound', 'SP', 'Pop')
print(festival2.nombre, festival2.pais, festival2.estilo_musical)

# Se pueden modificar los objetos
festival2.nombre = 'Benicassim'
print(festival2.nombre)

# Se puede eliminar un objeto con la palabra del
del festival1
# Esto da error porque el objeto ya está eliminado
# print(festival1)
