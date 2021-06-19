# Desarrollar programa que permita ingresar por pantalla los datos de N jugadores de voleibol (implemente try/except).
# Los datos a ingresar son:
# •	Posición De Juego	: 1-Delantero, 2-Zaguero, 3-Libero.
# •	Equipo Del Jugador	: 1-Ciutadella, 2-Teruel.
# •	Edad Del Jugador	: (Entre 14 y 28 años).
# Además, antes de terminar el programa debe imprimir los siguientes resultados:
# •	Cantidad De Jugadores Según Equipo:
#   o	Cantidad De Jugadores Del Equipo Ciutadella.
#   o	Cantidad De Jugadores De Equipo Teruel.
# •	Cantidad De Jugadores Según Posición:
#   o	Cantidad De Jugadores Con Posición Delantero.
#   o	Cantidad De Jugadores Con Posición Zaguero.
#   o	Cantidad De Jugadores Con Posición Libero.
# •	Cantidad De Jugadores Según Equipo y Posición:
#   o	Cantidad De Jugadores Con Posición Delantero De Ciutadella.
#   o	Cantidad De Jugadores Con Posición Delantero De Teruel.
#   o	Cantidad De Jugadores Con Posición Zaguero De Ciutadella.
#   o	Cantidad De Jugadores Con Posición Zaguero De Teruel.
#   o	Cantidad De Jugadores Con Posición Libero De Ciutadella.
#   o	Cantidad De Jugadores Con Posición Libero De Teruel.
# •	Promedio General De Edades De Todos Los Jugadores:

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


def digitarPosicion(i):
	while True:
		try:
			system("cls")
			print("1.Delantero")
			print("2.Zaguero")
			print("3.Libero")
			pos = int(input("Digite La Posicion De Juego Del Ingreso ("+str(i)+") : "))
			if pos!=1 and pos!=2 and pos!=3:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return pos
		except:
			print("\n--- La Posicion De Juego Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Posicion De Juego!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarEquipo(i):
	while True:
		try:
			system("cls")
			print("1.Ciutadela")
			print("2.Teruel")
			equ = int(input("Ingrese El Equipo La Vuelta ("+str(i)+") : "))
			if equ!=1 and equ!=2:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return equ
		except:
			print("\n--- El Equipo Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar El Equipo!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarEdad(i):
	while True:
		try:
			system("cls")
			eda = int(input("Digite La Edad Del Jugador ("+str(i)+") : "))
			if eda<14 or eda>28:
				print("\n--- La Edad Debe Estar Entre 14 y 28!! ---")
				system("pause")
			else:
				return eda
		except:
			print("\n--- La Edad Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Edad!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def ejecutarPrograma():
	global cciu, cter, suma
	global cdel, czag, clib
	global cdelciu, czagciu, clibciu
	global cdelter, czagter, clibter
	global pg

	cciu=0; cter=0; suma=0
	cdel=0; czag=0; clib=0
	cdelciu=0; czagciu=0; clibciu=0
	cdelter=0; czagter=0; clibter=0; pg=0

	ci = digitarCantidadIngresos() # Aqui llamo a la primera funcion.
	for i in range(1,ci+1):
		pos = digitarPosicion(i) # Aqui llamo a la segunda funcion.
		equ = digitarEquipo(i)   # Aqui llamo a la Tercera funcion.
		eda = digitarEdad(i)     # Aqui llamo a la cuarta  funcion.

		if equ==1:
			if pos==1:
				cdelciu = cdelciu+1
			elif pos==2:
				czagciu = czagciu+1
			else:
				clibciu = clibciu+1
		else:
			if pos==1:
				cdelter = cdelter+1
			elif pos==2:
				czagter = czagter+1
			else:
				clibter = clibter+1
			
		suma = suma+eda

	cciu = cdelciu+czagciu+clibciu
	cter = cdelter+czagter+clibter
	cdel = cdelciu+cdelter
	czag = czagciu+czagter
	clib = clibciu+clibter
	pg   = suma/ci


#------------------------------------------------------------------------------


def presentarResultados():
	system("cls")
	print("Cant. Jugadores Del Equipo Ciutadella: ",cciu)
	print("Cant. Jugadores Del Equipo Teruel    : ",cter)

	print("Cantidad De Jugadores Delanteros     : ",cdel)
	print("Cantidad De Jugadores Zagueros       : ",czag)
	print("Cantidad De Jugadores Liberos        : ",clib)

	print("Cantidad De Delanteros De Ciutadella : ",cdelciu)
	print("Cantidad De Delanteros De Teruel     : ",cdelter)
	print("Cantidad De Zagueros De Ciutadella   : ",czagciu)
	print("Cantidad De Zagueros De Teruel       : ",czagter)
	print("Cantidad De Liberos De Ciutadella    : ",clibciu)
	print("Cantidad De Liberos De Teruel        : ",clibter)

	print("Promedio General De Edades           : ",round(pg,1))


#------------------------------------------------------------------------------


ejecutarPrograma()
presentarResultados()