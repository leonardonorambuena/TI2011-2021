# Desarrollar programa que permita ingresar por pantalla 
# los datos de 10 mascotas. (implemente try/except). 
# Defina funciones para la digitación de cada dato.
# Los datos a ingresar son :
# 	Raza Del Perrito	: 1-Kiltro, 2-Boxer.
# 	Genero Del Perrito	: 1-Macho, 2-Hembra. 
# 	Edad Del Perrito 	: Entre 0 y 30 años (Edad humana).
# Antes de terminar el programa debe imprimir los siguientes resultados:
# •	Cantidad de perritos según raza:
#   o	Cantidad de KILTROS.
#   o	Cantidad de BOXERS.
# •	Cantidad de perritos según género:
#   o	Cantidad de MACHOS.
#   o	Cantidad de HEMBRAS.
# •	Suma de edades de perritos según raza:
#   o	Suma de edades de KILTROS.
#   o	Suma de edades de BOXERS.
# •	Suma de edades de perritos según género:
#   o	Suma de edades de MACHOS.
#   o	Suma de edades de HEMBRAS.
# •	Cantidad de perritos según raza y género:
#   o	Cantidad de KILTROS que son MACHOS.
#   o	Cantidad de KILTROS que son HEMBRAS.
#   o	Cantidad de BOXERS que son MACHOS.
#   o	Cantidad de BOXERS que son HEMBRAS.
# •	Suma de edades de perritos según raza y género:
#   o	Suma de edades de KILTROS que son MACHOS.
#   o	Suma de edades de KILTROS que son HEMBRAS.
#   o	Suma de edades de BOXERS que son MACHOS.
#   o	Suma de edades de BOXERS que son HEMBRAS.

from os import system

#------------------------------------------------------------------------------


def digitarRaza(i):
	while True:
		try:
			system("cls")
			print("1.Kiltro")
			print("2.Boxer")
			raz = int(input("Digite La Raza Del Ingreso ("+str(i)+") : "))
			if raz!=1 and raz!=2:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return raz
		except:
			print("\n--- La Raza Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Raza!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarGenero(i):
	while True:
		try:
			system("cls")
			print("1.Macho")
			print("2.Hembra")
			gen = int(input("Digite El Genero Del Ingreso ("+str(i)+") : "))
			if gen!=1 and gen!=2:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return gen
		except:
			print("\n--- El Genero Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar El Genero!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarEdad(i):
	while True:
		try:
			system("cls")
			eda = int(input("Digite La Edad Del Jugador ("+str(i)+") : "))
			if eda<0 or eda>30:
				print("\n--- La Edad Debe Estar Entre 0 y 30 Años!! ---")
				system("pause")
			else:
				return eda
		except:
			print("\n--- La Edad Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Edad!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def ejecutarPrograma():
	global ckil, cbox
	global cmac, chem
	global sedakil, sedabox
	global sedamac, sedahem
	global ckilmac, ckilhem
	global cboxmac, cboxhem
	global sedakilmac, sedakilhem
	global sedaboxmac, sedaboxhem

	ckil=0; cbox=0
	cmac=0; chem=0
	sedakil=0; sedabox=0
	sedamac=0; sedahem=0
	ckilmac=0; ckilhem=0
	cboxmac=0; cboxhem=0
	sedakilmac=0; sedakilhem=0
	sedaboxmac=0; sedaboxhem=0

	for i in range(1,11):
		raz = digitarRaza(i)
		gen = digitarGenero(i)
		eda = digitarEdad(i)
		
		if gen==1:
			if raz==1:
				ckilmac = ckilmac+1
				sedakilmac = sedakilmac+eda
			else:
				cboxmac = cboxmac+1
				sedaboxmac = sedaboxmac+eda
		else:
			if raz==1:
				ckilhem = ckilhem+1
				sedakilhem = sedakilhem+eda
			else:
				cboxhem = cboxhem+1
				sedaboxhem = sedaboxhem+eda
				
	ckil = ckilmac+ckilhem
	cbox = cboxmac+cboxhem
	cmac = ckilmac+cboxmac
	chem = ckilhem+cboxhem
	sedamac = sedakilmac+sedaboxmac
	sedahem = sedakilhem+sedaboxhem
	sedakil = sedakilmac+sedakilhem
	sedabox = sedaboxmac+sedaboxhem


#------------------------------------------------------------------------------


def presentarResultados():
	system("cls")
	print("Cantidad De Kiltros            : ",ckil)
	print("Cantidad De Boxers             : ",cbox)

	print("Cantidad De Machos             : ",cmac)
	print("Cantidad De Hembras            : ",chem)

	print("Suma De Edades De Kiltros      : ",sedakil)
	print("Suma De Edades De Boxers       : ",sedabox)

	print("Suma De Edades De Machos       : ",sedamac)
	print("Suma De Edades De Hembras      : ",sedahem)

	print("Cantidad De Kiltros Machos     : ",ckilmac)
	print("Cantidad De Kiltros Hembras    : ",ckilhem)
	print("Cantidad De Boxers Machos      : ",cboxmac)
	print("Cantidad De Boxers Hembras     : ",cboxhem)

	print("Suma Edades De Kiltros Machos  : ",sedakilmac)
	print("Suma Edades De Kiltros Hembras : ",sedakilhem)
	print("Suma Edades De Boxers Machos   : ",sedaboxmac)
	print("Suma Edades De Boxers Hembras  : ",sedaboxhem)


#------------------------------------------------------------------------------


ejecutarPrograma()
presentarResultados()