#Import libraries and declare variables
from collections import deque

turno = deque(["0", "X"])
tablero = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

def mostrar_tablero():
	print("")
	for fila in tablero:		
		print (fila)

def actualizar_tablero(posicion, jugador):
	tablero[posicion[0]][posicion[1]] = jugador

def rotar_turno():
	turno.rotate()
	return turno[0]

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1, int(columna)-1]

def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False

def ha_ganado(j):
	#compare board rows
	if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
		return True
	#compare the columns
	elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
		return True
	elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
		return True
	elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
		return True
	#compare the diagonals
	elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
		return True
	elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
		return True
	return False

def juego():
	mostrar_tablero()
	jugador = rotar_turno()
	while True:
		posicion = input("Juega {}, choose a position (row, column) from 1 to 3. 'exit' to exit".format(jugador))
		if posicion == 'exit':
			print ("Goodbye!!!")
			break
		try:
			posicion_l = procesar_posicion (posicion)			
		except:
			print ("Error, position {} is not valid. ".format(posicion))
			continue
		if posicion_correcta(posicion_l):
			actualizar_tablero(posicion_l, jugador)
			mostrar_tablero()
			if ha_ganado(jugador):
				print ("Player of {} has won!!!".format(jugador))
				break
			jugador = rotar_turno()
		else:
			print ("Position {} invalid".format(posicion))
	
juego()