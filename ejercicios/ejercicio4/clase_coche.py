# Ejercicio 4: CLASE COCHE
#     Modificar el código de la clase coche para que pueda ser llamado desde un nuevo fichero.
#     1.- El fichero de la clase se debe llamar clase_coche.py
#     2.- El Fichero del objeto desde donde llamar a la clase: objeto_coche.py
#     3.- Crear al menos una instancia para llamar al objeto y a la clase

# Creando la clase
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')

    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')


# Herencia: extendiendo la clase
class CocheElectrico(Coche):
    # El método __init__() para crear una clase hija
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.batery_size = 100
        self.nivel_carga = 0

    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche está cargado.')

    # Sobreescribir un método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina!')
