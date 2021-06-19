# from mate import solo_letras

text = input('Ingrese solo letras: ')

# if not solo_letras(text):
#     raise Exception('El sistema no funciona si ud ingresa numeros')

if text.isalpha() == False:
    raise Exception('El sistema no funciona si ud ingresa numeros')

print('Acá continua el programa')
    