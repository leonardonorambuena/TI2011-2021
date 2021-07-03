'''
    Desarrollar programa que permita el Ingreso de N números mayores a cero 
    dentro de una lista. Una vez ingresados, ordénelos, 
    digite un número cualquiera e identifique si se encuentra entre los valores registrados 
    indicando además su posición.
    (Indique la vuelta del ciclo +1 al ir digitando).
'''

x = int(input('Ingrese cantidad de veces a ejecutar: \n'))
mayores = []

for i in range(x):
    n = int(input('ingrese numero '+str(i + 1)+'\n'))
    if n > 0:
        mayores.append(n)

numero = int(input('Indique número a buscar: \n'))

if numero < 0:
    print('El numero ingresado no fue encontrado')

contador = 0
for i in range(len(mayores)):
    if mayores[i] == numero:
        print('El numero fue encontrado en el indice '+ str(i))
        contador += 1
        break

if contador == 0:
    print(f'El numero {numero} no fue encontrado')
    
