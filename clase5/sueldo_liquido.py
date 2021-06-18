'''
Generar script en Python que a partir del sueldo base se logre obtener el sueldo líquido, pero debe tener en cuenta los descuentos de salud y AFP.
Descuento De Afp     => Habitat(11%), Capital (13%).
Descuento De Salud => Fonasa(7%), Isapre(13%).
Impuesto A La Renta=> 5% Si el Sueldo Base supera el $1.200.000.
Sueldo Líquido          => Sueldo Base – Descto.Afp – Descto. Salud – Impuesto.
'''

def get_sb():
    try:
        return int(input('Ingrese sueldo base: \n'))
    except:
        print('Debe ingresar solo números')
        return None

def get_afp(sb):
    try:
        op = int(input('Afp: 1- Habitat (11%) 2- Capital (13%)'))
        # if op <= 0 or op > 2:
        #     print('Opción incorrecta eliga 1 0 2')
        #     return 0
        # res = 0
        if op == 1:
            return sb * .11
        elif op == 2:
            return sb * .13
        else:
            print('Opción incorrecta ingrese 1 o 2')
            return 0
    except:
        print('Debe elegir un número')
        return 0

def get_isapre(sb):
    try:
        op = int(input('Salud: 1- Fonasa (7%) 2- Isapre (13%)'))

        if op == 1:
            return sb * .07
        elif op == 2:
            return sb * .13
        else:
            print('Opción incorrecta ingrese 1 o 2')
            return 0
    except:
        print('Debe elegir un número')
        return 0

sb = None
imp = 0
afp = 0
isp = 0
while sb is None:
    sb = get_sb()
if sb > 1200000:
    imp = int(sb * (5)/100)
while afp == 0:
    afp = int(get_afp(sb))
while isp == 0:
    isp = int(get_isapre(sb))
sl = int(sb - imp - afp - isp)

from os import system

system('clear')
print(f'El Sueldo Base es : {sb}')
print('El descuento de salud es: ', isp)
print('El descuento de AFP es {}'.format(afp))
print('El descuento del impuesto a la renta es {}'.format(imp))
print('El sueldo liquido a pagar es: '+str(sl))




