import ejercicio6


# # Compresion de listas
# # numeros = [1,2,3,4,5]

# # cuadrados = [i ** 2 for i in numeros]


# # print(cuadrados)

# # solucion con compresion de listas
# pares_al_100 = [numero for numero in range(1, 101) if numero % 2 == 0]

# print(pares_al_100, end='\n\n\n')

# # sin compresion de listas
# pares_al_100 = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         pares_al_100.append(i)
# print(pares_al_100)
# print('Impares', end='\n\n\n')
# impares = [i for i in range(1,101) if i % 2 != 0]
# print(impares)

# # Sin operadores ternarios
# edad = 17

# mayor = False

# if edad > 18:
#     mayor = True
# else: # es solo ejemplo
#     mayor = False # es solo para ejemplo, redundante

# # Con operador ternario
# texto_mayor = 'Usted es mayor de edad' if edad > 17 else 'Usted es menor de edad' # esto no es lo mejor



# print(texto_mayor)

# mayor = edad > 17 # esto es lo mas lógico
