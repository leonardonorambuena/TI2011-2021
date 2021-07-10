'''
Desarrollar programa que permita el Ingreso de datos 3 productos, los cuales son:
    •Código   (número).
    •Nombre  (alfanumérico).
    •Marca  (1.Lider, 2.Jumbo).
    •Precio  (número) (Entre $100 y $25.000).
Genere un menú que permita ofrecer las siguiente opciones de acción:
1.Registrar Productos, 2.Listar Productos, 3.Estadística, 4.Salir.
Genere funciones para llevar a cabo la digitación de los datos y para representar el menú:
menuPrincipal(),  digitarCodigo(),    digitarNombre(),  digitarMarca(),
digitarPrecio(),   registrarProductos(),  listarProductos(),  estadística(), salir()
La estadística debe presentar los siguientes valores:
•promedio general de precios,
•promedio de precios de productos Líder
•promedio de precios de productos Jumbo.
'''
from os import sep, system
def registrarProductos():
    producto = {}
    system('clear')
    print('***** REGISTRO DE PRODUCTO *****', end='\n\n')
    producto['codigo'] = int(input('Ingrese un código: '))
    producto['nombre'] = input('Ingrese un nombre: ')
    producto['marca'] = int(input('Ingrese un marca: 1- Lider, 2- Jumbo'))
    producto['precio'] = int(input('Ingrese un precio: '))
    productos.append(producto)

def listarProductos():
    system('clear')
    print('***** REGISTRO DE PRODUCTO *****', end='\n\n')
    marcas = {1: 'Lider', 2: 'Jumbo'}
    if len(productos) == 0:
        print('No se han registrado productos')
        return
    for item in productos:
        for key in item.keys(): # el diccionario y estamos accediendo a sus claves
            val = item[key]
            if key == 'marca':
                val = marcas[item['marca']]
            end_chr = ' | ' if key != 'precio' else '\n' # operador ternario
            print(key, val, sep=' => ', end=end_chr)
    input()
def estadistica():
    # cont_general, cont_lider, cont_jumbo  = 0
    # acum_general, acum_lider, acum_jumbo = 0
    # prom_general, prom_lider, prom_jumbo = 0
    acum_general = 0
    for item in productos:
        for key in item.keys():
            if key == 'precio':
                acum_general += item[key]
    print('El promedio de valores de productos es', acum_general / len(productos))
    input()

productos = []
def menuPrincipal():
    op = None
    while len(productos) < 3:
        system('clear')
        print('1- Ingresar producto')
        print('2- Listar productos')
        print('3- Estadisticas')
        print('4- Salir')
        op = int(input('Ingrese la opción:\n'))
        if op == 1:
            registrarProductos()
        elif op == 2:
            listarProductos()
        elif op == 3:
            estadistica()
        elif op == 4:
            break
        else:
            print('Opción', op, 'No es válida') 


#print(__name__, 'desde el modulo ejercicio6')
if __name__ == '__main__':
    menuPrincipal()





