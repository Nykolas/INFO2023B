
# DEFINICION DE UNA CLASE (ES EL MOLDE DE LOS OBJETOS)
# LAS CLASES TIENEN ATRIBUTOS Y METODOS.

class Estudiante:

	def __init__(self,nom, edad, dni, legajo):
		self.nombre = nom
		self.edad = edad
		self.dni = dni
		self.legajo = legajo

	def getNombre(self):
		return self.nombre

	def setNombre(self,nuevo):
		self.nombre = nuevo

	def __str__(self):
		return f"Nombre: {self.nombre} \nEdad: {self.edad} \nDNI: {self.dni}"
#####################################

#COMO USO ESTE TIPO DE DATO
# e1 es un objeto con el formato de estudiante
e1 = Estudiante('nicolas',30,33000111,11999)

print(e1)

