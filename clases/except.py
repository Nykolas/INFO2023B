
valido = 1
while valido == 1:
	try:
		x = int(input("ingrese un numero: "))
		y = int(input("ingrese un numero: "))
		valido = 0
	except:
		print("INGRESO MAL UN DATO VUELVA A INTENTAR ")

res = x + y

print(f"el resultado es {res}")