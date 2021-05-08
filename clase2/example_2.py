number = int(input('Ingrese un número: '))

for i in range(number, -1, -1):
    if i == 0:
        print(i)
    else:
        print(i, end=',')