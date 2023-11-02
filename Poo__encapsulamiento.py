class Estudiante:

	def __init__(self,nom, edad, dni, legajo):
		self.__nombre = nom
		self.__edad = edad
		self.__dni = dni
		self.__legajo = self.__LegajoValido(legajo)

	def getNombre(self):
		return self.__nombre

	def setNombre(self,nuevo):
		self.__nombre = nuevo

	def getLegajo(self):
		return self.__legajo

	def setLegajo(self,nuevo):
		self.__legajo = self.__LegajoValido(nuevo)

	def __LegajoValido(self,nuevo):
		if nuevo < 90000:
			return nuevo
		else:
			return 0

	def __str__(self):
		return f"Nombre: {self.__nombre} \nEdad: {self.__edad} \nDNI: {self.__dni}\nLegajo: {self.__legajo}"

########################

e1 = Estudiante('Nicolas',34,33000111,95000)

print(e1)