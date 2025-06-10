
#Clase base/Clase padre

class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"{self.marca} {self.modelo}: está arrancando.")

#Subclase/Clase hija 1
class Auto(Vehículo):
    def abrir_maletero(self):
        print(f"{self.marca} {self.modelo}: maletero abierto")

#Subclase/Clase hija 2
class Moto(Vehículo):
    def hacer_caballito(self):
        print(f"{self.marca} {self.modelo}: haciendo el caballito")

if __name__ == "__main__":
    carro = Auto("Toyota", "Corolla")
    motocicleta = Moto("Yamaha", "MT-07")
    generico = Vehículo("OVNI", "UFO")

    carro.arrancar()
    motocicleta.arrancar()
    carro.abrir_maletero()
    generico.arrancar()
    
