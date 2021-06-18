# from os import system
# def saludar(msg = 'Bienvenidos'):
#     system('cls')
#     print('**********************************')
#     print(msg)
#     print('**********************************')

# def sumar(x, y):
#     if(type(x) and type(y) is not int):
#         raise ValueError('La función sumar solo debe tener parametros enteros')
#     print('la suma de ',x, 'y ', y, '=', x + y)

# sumar(10, 25)
# try:
#     sumar('hola', 'como estas')
# except ValueError as e:
#     print(e)
# # x = 10
# # z = 10

# # def sumar(x, z):
# #     return x + z;

# # print(sumar(x, z))


# saludar()

# saludar('Ingreso de producto')

# saludar(56)

# # print(sumar(5,10))

# def imprimir():
#     print('No tengo ningún parametro')


# imprimir()

# var = 1
# def scopeTest():
#     global var
#     print(var)
#     var = 2
# scopeTest()

# scopeTest()

from modulo1 import pi, multiplicar

print(pi)

print(multiplicar(5,5))