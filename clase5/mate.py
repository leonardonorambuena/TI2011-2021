
obj = {'altura': 0, 'ancho': 0}

def sumar(x, y):
    obj['altura'] = x ** y
    obj['ancho'] = y // x
    return obj

def es_mayor(edad):
    return edad > 18



from os import system
import platform

def limpiar_pantalla_con_retorno():
    if 'macOS' in platform.platform():
        return 'clear'
    return 'cls'

def limpiar_pantalla():
    if 'macOS' in platform.platform():
        system('clear')
    else:
        system('cls')

def solo_letras(t):
    for i in t:
        if i.isdigit():
            return False
    return True



