# Desarrollar programa que permita ingresar por pantalla 
# los datos N vehículos.
# (implemente try/except). Defina funciones para la digitación de cada dato.
# Los datos a ingresar son:
# •	Marca de vehículo	: 1-Nissan, 2-Chevrolet, 3-Hyundai.
# •	Licencia Del Chofer	: 1-Clase A, 2-Clase B.
# Antes de terminar el programa debe imprimir los siguientes resultados:
# Además, al término del proceso debe imprimir:
# •	Cantidad De Vehículos NISSAN.
# •	Cantidad De Vehículos CHEVROLET.
# •	Cantidad De Vehículos HYUNDAI.
# • 	Cantidad De Licencias Clase A.
# •	Cantidad De Licencias Clase B. 
# •	Cantidad De Licencias Clase A Asociadas a NISSAN.
# •	Cantidad De Licencias Clase B Asociadas a NISSAN. 
# •	Cantidad De Licencias Clase A Asociadas a CHEVROLET.
# •	Cantidad De Licencias Clase B Asociadas a CHEVROLET
# •	Cantidad De Licencias Clase A Asociadas a HYUNDAI.
# •	Cantidad De Licencias Clase B Asociadas a HYUNDAI.

from os import system

#------------------------------------------------------------------------------

def digitarCantidadIngresos():
	while True:
		try:
			system("cls")
			ci = int(input("¿Cuantos Ingresos Desea Realizar? : "))
			if ci<=0:
				print("\n--- Los Ingresos Deben Ser > 0!! ---\n")
				system("pause")
			else:
				return ci
		except:
			print("\n--- La Cantidad De Ingresos Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Cantidad De Ingresos!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarMarca(i):
	while True:
		try:
			system("cls")
			print("1.Nissan")
			print("2.Chevrolet")
			print("3.Hyundai")
			mar = int(input("Digite La Marca Del Ingreso ("+str(i)+") : "))
			if mar!=1 and mar!=2 and mar!=3:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return mar
		except:
			print("\n--- La Marca Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Marca!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarLicencia(i):
	while True:
		try:
			system("cls")
			print("1.Clase A")
			print("2.Clase B")
			cla = int(input("Digite La Clase Del Ingreso ("+str(i)+") : "))
			if cla!=1 and cla!=2:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return cla
		except:
			print("\n--- La Clase De Licencia Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Clase De Licencia!! ---\n")
			system("pause")


#------------------------------------------------------------------------------



def ejecutarPrograma():
	global cnis, cche, chyu
	global ca, cb
	global canis, cache, cahyu
	global cbnis, cbche, cbhyu

	cnis=0; cche=0; chyu=0
	ca=0; cb=0
	canis=0; cache=0; cahyu=0
	cbnis=0; cbche=0; cbhyu=0

	ci = digitarCantidadIngresos() # Aqui llamo a la primera funcion.
	for i in range(1,ci+1):
		mar = digitarMarca(i)
		cla = digitarLicencia(i)

		if cla==1:
			if mar==1:
				canis = canis+1
			elif mar==2:
				cache = cache+1
			else:
				cahyu = cahyu+1
		else:
			if mar==1:
				cbnis = cbnis+1
			elif mar==2:
				cbche = cbche+1
			else:
				cbhyu = cbhyu+1
				
	ca = canis+cache+cahyu
	cb = cbnis+cbche+cbhyu
	cnis = canis+cbnis
	cche = cache+cbche
	chyu = cahyu+cbhyu


#------------------------------------------------------------------------------


def presentarResultados():
	system("cls")
	print("Cant. De Vehiculos Nissan                   : ",cnis)
	print("Cant. De Vehiculos Chevrolet                : ",cche)
	print("Cant. De Vehiculos Hyundai                  : ",chyu)

	print("Cant. De Vehiculos Con Licencia Clase A     : ",ca)
	print("Cant. De Vehiculos Con Licencia Clase B     : ",cb)

	print("Cant. De Vehiculos Nissa     Con Lic.Clase A: ",canis)
	print("Cant. De Vehiculos Nissa     Con Lic.Clase B: ",cbnis)

	print("Cant. De Vehiculos Chevrolet Con Lic.Clase A: ",cache)
	print("Cant. De Vehiculos Chevrolet Con Lic.Clase B: ",cbche)

	print("Cant. De Vehiculos Hyundai   Con Lic.Clase A: ",cahyu)
	print("Cant. De Vehiculos Hyundai   Con Lic.Clase A: ",cbhyu)


#------------------------------------------------------------------------------


ejecutarPrograma()
presentarResultados()