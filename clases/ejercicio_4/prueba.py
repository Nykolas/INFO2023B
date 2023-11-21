
class PruebaTiempo:
	def __init__(self, tiempo):
		self.tiempo = tiempo

	def probarTiempo(self):
		mal = list()
		if self.tiempo.getHora() > 23 or self.tiempo.getHora() < 0:
			mal.append("HORA")
		if self.tiempo.getMinutos() > 59 or self.tiempo.getMinutos() < 0:
			mal.append("MINUTOS")
		if self.tiempo.getSegundos() > 59 or self.tiempo.getSegundos() < 0:
			mal.append("SEGUNDOS")
		return mal
		

	def mostrarTiempo(self):
		print (f'el tiempo actual es: {self.tiempo.getHora()} HH-{self.tiempo.getMinutos()} MM-{self.tiempo.getSegundos()} SS')

	def cambiarHora(self, nueva):
		self.tiempo.setHora(nueva)

	def cambiarMinutos(self,nuevos):
		self.tiempo.setMinutos(nuevos)

	def cambiarSegundos(self,nuevos):
		self.tiempo.setSegundos(nuevos)
