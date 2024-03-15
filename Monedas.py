print('<<<<<BIEMVENIDO A NUESTRO CONVERSOR DE MONEDAS>>>>>')

while True:
    opciones = input('\n1. convertir\n2.finalizar\n ->')
    if opciones == '1':
        moneda = input('Ingrese la moneda a convertir: ')
        valor = int(input('Ingrese el valor a convertir: '))
        if moneda == 'P' or 'p': 
            print('El valor de',valor ,'pesos es:', valor * 3.800, 'dolares')
        else:
            print('No se reconoce la moneda ingresada')
    if opciones == '2':
        print('<<<GRACIAS POR TU TIEMPO>>>')
        
        break
