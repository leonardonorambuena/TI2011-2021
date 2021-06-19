# Desarrollar programa que permita ingresar por pantalla 
# los datos de N jugadores de fútbol (implemente try/except). 
# Defina funciones para la digitación de cada dato.
# Los datos a ingresar son:
#   •	Posición De Juego	: 1-Delantero, 2-Mediocampista, 3-Defensa, 4.Portero.
#   •	Edad Del Jugador	: (Entre 10 y 50).
# Los jugadores serán clasificados y dicha clasificación dependerá de la edad:
#   •	De tener una edad entre 10 y 17, será clasificado como juvenil.
#   •	De tener una edad entre 18 y 50 será clasificado como adulto.
# Antes de terminar el programa debe imprimir los siguientes resultados:
#   •	Cantidad Total De Jugadores.
#   •	Promedio De Edad De Todos Los Jugadores.
#   •	Cantidad Total De Jugadores Juveniles
#   •	Promedio De Edad De Jugadores juveniles.
#   •	Cantidad De Jugadores Adulto.
#   •	Promedio De Edad De Jugadores Adulto.
#   •	Cantidad De Delanteros.
#   •	Promedio De Edad De Delanteros.
#   •	Cantidad De Mediocampistas.
#   •	Promedio De Edad De Mediocampistas.
#   •	Cantidad De Defensas.
#   •	Promedio De Edad De Defensas.
#   •	Cantidad De Porteros.
#   •	Promedio De Edad De Porteros.

from os import system
from mate import limpiar_pantalla

#------------------------------------------------------------------------------

def digitarCantidadIngresos():
	while True:
		try:
			limpiar_pantalla()
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
			limpiar_pantalla()
			print("1.Delantero")
			print("2.Medicampista")
			print("3.Defensa")
			print("4.Portero")
			pos = int(input("Digite La Posicion De Juego Del Ingreso ("+str(i)+") : "))
			if pos!=1 and pos!=2 and pos!=3 and pos!=4:
				print("\n--- Error De Opcion!! ---\n")
				system("pause")
			else:
				return pos
		except:
			print("\n--- La Posicion De Juego Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Posicion De Juego!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def digitarEdad(i):
	while True:
		try:
			limpiar_pantalla()
			eda = int(input("Digite La Edad Del Jugador ("+str(i)+") : "))
			if eda<10 or eda>50:
				print("\n--- La Edad Debe Estar Entre 10 y 50!! ---")
				system("pause")
			else:
				return eda
		except:
			print("\n--- La Edad Debe Tener Solo Numeros!! ---")
			print("--- Error Al Intentar Almacenar La Edad!! ---\n")
			system("pause")


#------------------------------------------------------------------------------


def ejecutarPrograma():
	global cjuv, cadu, cdel, cmed, cdef, cpor
	global sjuv, sadu, sdel, smed, sdef, spor, stot
	global pjuv, padu, pdel, pmed, pdef, ppor, pg

	cjuv=0; cadu=0; cdel=0; cmed=0; cdef=0; cpor=0
	sjuv=0; sadu=0; sdel=0; smed=0; sdef=0; spor=0; stot=0
	pjuv=0; padu=0; pdel=0; pmed=0; pdef=0; ppor=0; pg=0

	ci = digitarCantidadIngresos() # Aqui llamo a la primera funcion.
	for i in range(1,ci+1):
		pos = digitarPosicion(i)   # Aqui llamo a la segunda funcion.
		eda = digitarEdad(i)       # Aqui llamo a la tercera funcion.
		if eda>=10 and eda<=17:
			cjuv = cjuv+1
			sjuv = sjuv+eda
			pjuv = sjuv/cjuv
		
		if eda>=18 and eda<=50:
			cadu = cadu+1
			sadu = sadu+eda
			padu = sadu/cadu
		
		if pos==1:
			cdel = cdel+1
			sdel = sdel+eda
			pdel = sdel/cdel
		elif pos==2:
			cmed = cmed+1
			smed = smed+eda
			pmed = smed/cmed
		elif pos==3:
			cdef = cdef+1
			sdef = sdef+eda
			pdef = sdef/cdef
		else:
			cpor = cpor+1
			spor = spor+eda
			ppor = spor/cpor

	stot = sjuv+sadu
	pg = stot/ci


#------------------------------------------------------------------------------


def presentarResultados():
	limpiar_pantalla()
	print("Cantidad Total De Jugadores : ",(cjuv+cadu))
	print("Promedio General De Edades  : ",round(pg,1))
	print("Cantidad De Juveniles       : ",cjuv)
	print("Promedio De Juveniles       : ",round(pjuv,1))
	print("Cantidad De Adultos         : ",cadu)
	print("Promedio De Adultos         : ",round(padu,1))
	print("Cantidad De Delanteros      : ",cdel)
	print("Promedio De Delanteros      : ",round(pdel,1))
	print("Cantidad De Mediocampistas  : ",cmed)
	print("Promedio De Mediocampistas  : ",round(pmed,1))
	print("Cantidad De Defensas        : ",cdef)
	print("Promedio De Defensas        : ",round(pdef,1))
	print("Cantidad De Porteros        : ",cpor)
	print("Promedio De Porteros        : ",round(ppor,1))


#------------------------------------------------------------------------------


ejecutarPrograma()
presentarResultados()