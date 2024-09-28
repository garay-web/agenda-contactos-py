

def mostrar_menu():
    print('\nAgenda de contactos:')
    print('\n1.- Agregar nuevo contacto')
    print('\n2.-Eliminar contacto existente')
    print('\n3.- Buscar contacto')
    print('\n4.- Lista de contactos')
    print('\n5.- Salir del programa\n')
    print('-'*24)
    
def  agrergar_contacto(agenda):
    nombre = input('Por favor introduzca el nombre completo del contacto: ')
    telefono = input('Por favor introduzca el teléfono del contacto: ')
    email = input('Por favor introduzca el email del contacto: ')
    agenda[nombre] = {'telefono':telefono, 'email':email}
    print(f'\n¡Se ha agregado el contacto _"{nombre}"_ exitosamente!')

def eliminar_contacto(agenda):
    nombre = input('Ingrese el nombre de la agenda que desea eliminar:')
    if nombre in agenda:
        del agenda[nombre]
        print(f'El contacto de {nombre} ha sido eliminado correctamente')
    else:
        print(f'No se ha encontrado un contacto con el nombre {nombre}')

def buscar_contacto(agenda):
    nombre = input('Ingrese el nombre del contacto que está buscando')
    if nombre in agenda:
        print(f'Nombre: {nombre}')
        print(f'Teléfono: {agenda[nombre]['telefono']}')
        print(f'Email: {agenda[nombre]['email']}')
    else:
        print(f'El contacto {nombre} no ha sido encotrado en la agenda')

def listar_contactos(agenda):
    if agenda:
        print('Lista de contactos: ')
        for nombre, info in agenda.items():
            print(f'Nombre: {nombre}')
            print(f'Teléfono: {info['telefono']}')
            print(f'Email: {info['email']}')
            print('-'*20)
    else:
        print('\n')
        print( '-'*28,'¬')
        print('|< La agenda aún está vacía >|') 
        print('-'*30)


def  agenda_contactos():
    agenda = {}


    while True:
        mostrar_menu()
        opcion = input('Por favor elija un opción: ')
        print('\n')
        if opcion == '1':
            agrergar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            listar_contactos(agenda)
        elif opcion == '5':
            print('Saliendo de la agenda de contactos...¡Nos vemos!')
            break
        else:
            print('Por favor elija una opcion válida(del 1 al 5)')

agenda_contactos()
