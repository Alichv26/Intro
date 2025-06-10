
#Herencia multinivel

#Nivel 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")

#Nivel 2
class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID empleado: {self.id_empleado}")


#Nivel 3
class Profesor(Empleado):
    def __init__(self, nombre, edad, id_empleado, asignatura):
        super().__init__(nombre, edad, id_empleado)
        self.asignatura = asignatura

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")


class Miscelaneo(Empleado):
    def __init__(self, nombre, edad, id_empleado, zona):
        super().__init__(nombre, edad, id_empleado)
        self.zona = zona
        self.horario = "Diurno"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Zona: {self.zona}")

prof = Profesor("Ana", "35", "EMP0001", "POO")
prof2 = Profesor("Diego", "35", "EMP0002", "POO")
prof3 = Profesor("Jeff", "35", "EMP0003", "POO")
prof4 = Profesor("Denyie", "35", "EMP0004", "POO")


misc1 = Miscelaneo("Maria", 28, "M100", "Edificio B3")
misc2 = Miscelaneo("Lin", 28, "M101", "Edificio B6")

empleados = [prof, misc1, prof2, misc2, prof3, prof4]

for e in empleados:
    e.mostrar_info()
    print()


emp = Empleado("Ana", "35", "EMP0001")
emp.mostrar_info()

persona = Persona("Yordey", "17")
persona.mostrar_info()
