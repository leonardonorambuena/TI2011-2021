deuda = 10000

monto = int(input('Ingrese monto a pagar: '))

saldo = deuda - monto
if saldo == 0:
    print('no tiene deudas')
elif saldo > 0:
    print(f'tu deuda es: {saldo}')
else:
    print(f'Tu vuelto es: {-saldo}')
    