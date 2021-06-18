import os as operative_system

numbers = int(input('Ingrese cantidad de numeros a ingresar: \n'))

# print('ingrese un dato')
# v = input() // leer
# v = input('ingrese un dato') -> escribiendo por pantalla y esta leyendo lo que ingrese el usuario
result = []
for i in range(numbers):
    #v = int(input(f'Ingrese Numero {i+1} \n'))
    result.append(int(input(f'Ingrese Numero {i+1} \n')))

# vuelta 1 -> 4 -> result[4]
# vuelta 2 -> 5 -> result[4, 5]

operative_system.system('cls') # clear en linux o mac

print('Los numeros al cuadrado son: ')
for n in result:
    print(n, 'al cuadrado es:',n ** 2)

print(result)

