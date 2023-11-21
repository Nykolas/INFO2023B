from tiempo import Tiempo 
from prueba import PruebaTiempo


def menu():
	print("HOLA\n")
	print("lo primero es ingresar una hora\n")
	h = int(input("ingrese la hora en formato HH\t"))
	
	try:
		m = int(input("ingrese los minutos MM, sino, simplemente presione enter\t"))
	except:
		print("como no puso los MM los segundos tb seran NONE")
		m = 0
		s = 0

	if m != 0:
		try:
			s = int(input("ingrese los segundos SS, sino, simplemente presione enter\t"))
		except:
			s = 0

	t = Tiempo(h,m,s)	
	prueba = PruebaTiempo(t)

	while True:
		print("MENU:\n 1:analizar,\n 2:cambiar hora,\n 3: cambiar mm,\n 4:cambiar segundos\n 5:salir")
		o = int(input(""))
		if o == 1:
			mal = prueba.probarTiempo()
			if not mal:
				print("ESTA GENIAL!!!!")
			else:
				print(f'TENES MAL CARGADO ESTO: \n')
				print(' '.join(mal))

		elif o == 2:
			prueba.cambiarHora(int(input("INGRESE NUEVA HORA\t")))
		elif o == 3:
			prueba.cambiarMinutos(int(input("INGRESE NUEVOS MM\t")))
		elif o == 4:
			prueba.cambiarSegundos(int(input("INGRESE NUEVOS SS\t")))
		else:
			break

		print("ASI TE QUEDO LA HORA ;) \n")
		prueba.mostrarTiempo()
		
menu()