list_nombre = []
list_Tipo = []
list_area = []
list_permiso = []
list_valor = []

import os
def fnt_limpiar():
    os.system('cls')
    print('Autor: Santiago Barrera Arias')
    print('Fecha: 25/04/2024\n\n')
def calcular_area(largo, ancho):
    area = largo * ancho
    return area
def fnt_registrar(nombre, Tipo, area, permiso, valor):
    if nombre == ' ' or Tipo == ' ' or area == ' ' or permiso == ' ' or valor == ' ':
        print('No se puede registrar, faltan datos')
    else:
        list_nombre.append(nombre)
        list_Tipo.append(Tipo)
        list_area.append(area)
        list_permiso.append(permiso)
        list_valor.append(valor)
def fnt_selector(opcion):
    global sw
    fnt_limpiar()
    if opcion == '1':
            print('\n<<< SELECCIONE SU TIPO DE LOTE >>>')
            opcion2 = input('\na. Lote Urbano\nb. Lote Comercial\nc. Campestre\n--> ')
            if opcion2 == 'a' or opcion == 'A':
                fnt_limpiar()
                Tipo = print('\n<<< LOTE URBANO >>>')
                nombre = input('Ingrese su nombre\n--> ')
                largo = int(input('Ingrese la medida de largo\n--> '))
                ancho = int(input('Ingrese la medida de ancho\n--> '))
                area = calcular_area(largo, ancho)
                valor = area * 25000
                permiso = valor * 0.45
                pagar = valor + permiso
                print(f'\nPersonal {nombre} el Área de su lote es: {area}m2\nValor del permiso: {permiso} \nEl valor total a pagar es de:', pagar)
                input('\nLa información fue registrada con éxito\nPresione <ENTER> para continuar')
            elif opcion2 == 'b' or opcion == 'B':
                fnt_limpiar()
                Tipo = print('\n<<< LOTE COMERCIAL >>>')
                nombre = input('Ingrese su nombre\n--> ')
                largo = int(input('Ingrese la medida de largo\n--> '))
                ancho = int(input('Ingrese la medida de ancho\n--> '))
                area = calcular_area(largo, ancho)
                valor = area * 60000
                permiso = valor * 0.75
                pagar = valor + permiso
                print(f'\nPersonal {nombre} el Área de su lote es: {area}m2\nValor del permiso: {permiso} \nEl valor total a pagar es de:', pagar)
                input('La información fue registrada con éxito\nPresione <ENTER> para continuar')
            elif opcion2 == 'c' or opcion == 'C':
                fnt_limpiar()
                Tipo = print('\n<<< LOTE CAMPESTRE >>>')
                nombre = input('Ingrese su nombre\n--> ')
                largo = int(input('Ingrese la medida de largo\n--> '))
                ancho = int(input('Ingrese la medida de ancho\n--> '))
                area = calcular_area(largo, ancho)
                valor = area * 15000
                permiso = valor * 0.15
                pagar = valor + permiso
                print(f'\nPersonal {nombre} el Área de su lote es: {area}m2\nValor del permiso: {permiso} \nEl valor total a pagar es de:', pagar)
                input('La información fue registrada con éxito\nPresione <ENTER> para continuar')
                fnt_registrar(nombre, Tipo, area, permiso, valor)
            
            
    elif opcion == '2':
        fnt_limpiar()
        print('\n<<< LISTA DE LOTES >>>')
        for i in range(len(list_nombre)):
            print(f'Nombre: {list_nombre[i]}\nÁrea: {list_area[i]}\nTipo de Lote: {list_Tipo[i]}\nPermiso: {list_permiso[i]}\nValor Total: {list_valor[i]}')
        enter = input('Presione <ENTER> para continuar')
        
    elif opcion == '3':
        print('PROGRAMA FINALIZADO\n')
        sw = False
sw = True
while sw == True:  
    fnt_limpiar()
    opcion = input('<<< MENÚ PRINCIPAL >>>\n\n1. AGREGAR NUEVO LOTE\n2. MOSTRAR LOTES\n3. SALIR\n--> ')
    fnt_selector(opcion)
    