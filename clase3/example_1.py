# import math
# # 17.221.223-5
# # int -> 171212121 dv = char 1
# try:
#     x = float(input('ingrese el valor de x \n'))
#     y = math.sqrt(x)
#     print('la raíz cuadrada de',x, 'es:',y)
# except:
#     print('No puede ingresar números negativos')
# while True:
#     try:
#         x = int(input('ingrese un número'))
#     except:
#         print('Ingrese solo números')
#     else:
#         print('El proceso fue correcto')
#     finally:
#         print('Me ejecuto siempre al finalizar independiente si caigo en una excepción')




try:
    x = int(input('ingrese un n \n'))
    assert x > 0
    if x > 10:
        raise Exception('El número no puede ser mayor a 10')
except AssertionError:
    print('No debe ingresar número negativos')
except ValueError as e:
    print(e)
except BaseException as e:
    print(e)