name = 'leonardo noRaMbUENA'

print(name.lower()) # leonardo norambuena

print(name.upper()) # LEONARDO NORAMBUENA

print(name.title()) # Leonardo Norambuena

print('inacap'.find('ap')) # 4

print('inacap'.find('p')) # 5

print('inacap'.index('p'), 'ejemplo con index') # 5

print('inacap'.find('pa')) # -1

# print('inacap'.index('pa')) # -1 ValueError

lista = ['a', 'b', 'c']
try:
    print(lista[2])
except:
    print('El indice no existe')
