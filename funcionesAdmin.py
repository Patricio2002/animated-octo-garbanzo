from productos import *
from admin import Administrador
from excepciones import *

maquina = MaquinaExpendedora()
product = []

def validarCantidades (cantidades):
    if cantidades<=0:
        print("Ingrese cantidad valida")
        return False
    else:
        return True

def actualizarDatos(lista):
    act = []
    for i in range(len(lista)):
        act.append(lista[i].retornarInfo())
    maquina.actualizarCSV(act)

#función que lee todos los datos nuevos del producto y lo sube al csv
def añadirProducto(lista):
    global product
    try: 
        tipo = int(input("¿Qué clase de producto va a ingresar?\t1.Botana\t2.Bebida\t3.Dulce: \n"))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!\n")
    else:
        if int(tipo) == 1 or int(tipo) == 2 or int(tipo) == 3:

            marca = input("Ingrese el nombre del producto: ")
            try:
                verifCadena(marca)
            except cadenaVacia:
                print('No ingrese cadenas vacías')
                return 1
            try:
                cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
                while validarCantidades(cantidad)==False:
                    cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
                    continue
            except ValueError: 
                print("\nIntroduzca solo numeros!!!\n")
                return 1

            try: 
                precio = int(input("Ingrese el  precio del producto: "))
                while validarCantidades(precio)==False:
                    precio= int(input("Ingrese el precio del producto: "))
                    continue
            except ValueError: 
                print("\nIntroduzca solo numeros!!!\n")
                return 1

            if int(tipo) == 1:
                tipo = "Botana"
                try:
                    gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
                    while validarCantidades(gramos)==False:
                        gramos= int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
                        continue
                except ValueError: 
                    print("\nIntroduzca solo numeros!!!\n")
                    return 1
                
                sabor = input("Ingrese el sabor del producto: ")

            elif int(tipo) == 2:
                tipo = "Bebida"
                try:
                    gramos = int(input("Ingrese los mililitros que contiene el producto: "))
                    while validarCantidades(gramos)==False:
                        gramos= int(input("Ingrese los mililitros que contiene el producto: "))
                        continue 
                except ValueError: 
                    print("\nIntroduzca solo numeros!!!\n")
                    return 1
                
                sabor = input("Ingrese el sabor del producto: ")

            else:
                tipo = "Dulces"
                try:
                    gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
                    while validarCantidades(gramos)==False:
                        gramos= int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
                        continue
                except ValueError: 
                    print("\nIntroduzca solo numeros!!!\n")
                    return 1
                
                sabor = []
                while 1:
                    try:
                        sabor.append(input("Ingrese el sabor del producto: "))
                        verifCadena(sabor)
                    except cadenaVacia:
                        print('No ingrese cadenas vacias')
                        return 1
                    try:
                        anadir=int(input("¿Desea ingresar otro sabor?\n1.Si\n2.No\n"))
                    except ValueError: 
                        print("\nIntroduzca solo numeros!!!\n")
                        return 1
                    else:
                        if int(anadir) == 1:
                            continue
                        elif int(anadir) == 2:
                            sabor = '. '.join(sabor)
                            break
                        else:
                            print("Ingrese un valor valido")
            lista.append(globals()[tipo](len(lista)+1,marca,cantidad,precio,sabor,gramos,tipo))
            actualizarDatos(lista)
        else:
            print("Ingrese valores validos")
            return 0
    


#función que modifica un valor de un atributo y lo envía a la función actualizarDatos
def modificarProducto(lista):
    try:
        clave = int(input('Ingrese la clave del producto que desea modificar: '))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        clave = clave-1
        modif = int(input('ingrese el dato que desee cambiar:\n\
    1. Nombre\n2. Costo\n3. Cantidad\n4. Gramos\n5. Sabor\n'))
        
        if modif == 1:
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            try:
                verifCadena(nuevoNombre)
            except cadenaVacia:
                print('No ingrese cadenas vacías')
                return 1
            else:
                lista[clave].nombre = nuevoNombre

        elif modif == 2:
            try:
                nuevoCosto = int(input("Ingrese el nuevo costo: "))
            except ValueError:
                print('\nIntroduzca solo números')
            else:
                while validarCantidades(nuevoCosto)==False:
                    try:
                        nuevoCosto= int(input("Ingrese el nuevo costo: "))
                        continue
                    except ValueError:
                        print('Introduzca solo números!!!')
                lista[clave].costo = nuevoCosto

        elif modif == 3:
            try: 
                nuevaCantidad = int(input("Ingrese cuantas unidades del producto va a agregar: "))
            except ValueError:
                print('\nIntroduzca solo numeros!!!')
                return 1
            while validarCantidades(nuevaCantidad)==False:
                try: 
                    nuevaCantidad = int(input("Ingrese cuantas unidades del producto va a agregar: "))
                except ValueError:
                    print('\nIntroduzca solo numeros!!!')
                continue
            lista[clave].cantidad = nuevaCantidad

        elif modif == 4:
            try:
                nuevoGramo = int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
            except ValueError:
                print('\nIntroduzca solo numeros!!!')
                return 1
            else:
                if(lista[clave]._tipo == 'Bebida'):
                    while validarCantidades(nuevoGramo)==False:
                        try:
                            nuevoGramo= int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
                            continue
                        except ValueError:
                            print('\nIntroduzca solo numeros!!!')
                    else:
                        lista[clave].mililitros = nuevoGramo
                else:
                    while validarCantidades(nuevoGramo)==False:
                        try:
                            nuevoGramo= int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
                            continue
                        except ValueError:
                            print('\nIntroduzca solo numeros!!!')
                    else:
                        lista[clave].gramos = nuevoGramo

        elif modif == 5:
            try:
                nuevoSabor = input("Ingrese el nuevo sabor del producto: ")
                verifCadena(nuevoSabor)
            except cadenaVacia:
                print('No ingrese cadenas vacias')
            else:
                lista[clave].sabor = nuevoSabor

        actualizarDatos(lista)
        
def eliminarProducto(lista):
    try: 
        clave = int(input('Ingrese la clave del producto que desea eliminar'))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        while validarCantidades(clave)==False or clave>=len(lista)+2:
                 clave= int(input("Ingrese clave existente: "))
                 continue
        lista.pop(clave-1)
        for i in range(len(lista)):
            lista[i].clave = i+1
        actualizarDatos(lista)

#función que genera un nuevo admin en administradores.csv
def crearAdmin():
    nombre = input("Ingrese el nombre del nuevo administrador: ")
    contraseña = input("Ingrese su contraseña: ")
    if len(nombre) != 0 or len(contraseña) != 0:
        nuevoAdmin = Administrador(nombre, contraseña)
        nuevoAdmin.nuevoAdmin()
    else:
        'No se puede ingresar cadenas vacias'

#función que valida si existe la cuenta y contraseña del admin que desea ingresar
def iniciarSesion(lista):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    admin = Administrador(usuario, contraseña)
    validar = admin.validacion()
    print("\n")
    if validar == 1:
        while(1):
            try:
                opcion = int(input(f"Bienvenido {usuario}. \n¿Qué desea hacer?\n\n\
1. Añadir producto\n\
2. Eliminar producto\n\
3. Modificar información de un producto\n\
4. Crear nuevo administador\n\
5. Cerrar Sesión (Volver al menú inicial)\n"))
                print("\n")
            except ValueError: 
                print("\nIntroduzca solo numeros!!!")
            else:
                if opcion == 1:
                    añadirProducto(lista)
                elif opcion == 2:
                    eliminarProducto(lista)
                elif opcion == 3:
                    modificarProducto(lista)
                elif opcion == 4:
                    crearAdmin()
                elif opcion == 5:
                    break
                else:
                    print('Ingrese valores validos')
    else:
        print("Contraseña o usuario erroneos")