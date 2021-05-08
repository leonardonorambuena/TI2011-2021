number = int(input('Ingrese cantidad de impares a mostrar: '))

# alternativa 1
impares = []
for n in range(1, number + 1):
    if not n  % 2 == 0:
        impares.append(n)

#  -3    -2   -1
#  0   1  2 
# [1 , 2, 3]

for n in impares:
    if n == impares[-1]:
        print(n)
    else:
        print(n, end=',')

# alternativa 2
# for n in range(1, number + 1):
#     if n  % 2 != 0:
#         print(n, end='')

# alternativa 3 impares con incremento
# for n in range(1, number + 1, 2):
#     print(n, end='')

# for n in range(2, number + 1, 2):
#     print(n, end='')