
#HERENCIA, LA USAMOS CUANDO TENGO OBJETOS QUE COMPARTEN ATRIUBTOS Y METODOS
class Persona:
	def __init__(self,nom, edad, dni):
		self.nombre = nom.upper()
		self.edad = edad
		self.dni = dni

	def getNombre(self):
		return self.nombre

	def setNombre(self,nuevo):
		self.nombre = nuevo

	def __str__(self):
		return f"Nombre: {self.nombre} \nEdad: {self.edad} \nDNI: {self.dni}"

class Estudiante(Persona):
	def __init__(self,nom, edad, dni, legajo):
		super().__init__(nom,edad,dni)
		self.legajo = legajo

	def __str__(self):
		return f"Alumno:\n{super().__str__()}\nLegajo: {self.legajo}"

#####################################
class Profesor(Persona):
	def __init__(self, nom, edad, dni, materia):
		super().__init__(nom,edad,dni)
		self.materia = materia

	def __str__ (self):
		return f"Profesor:\n{super().__str__()}\nMateria que dicta: {self.materia}"

#########################

e1 = Estudiante('nicolas',30,33000111,11999)
print(e1)
print("-----------------------")
p1 = Profesor('Franco',24,45000777,'POO')
print(p1)