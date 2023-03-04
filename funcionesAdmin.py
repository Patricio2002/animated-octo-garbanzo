from productos import *
from admin import Administrador

maquina = MaquinaExpendedora()
product = []

def actualizarDatos(lista):
    act = []
    for i in range(len(lista)):
        act.append(lista[i].retornarInfo())
    maquina.actualizarCSV(act)

def añadirProducto():
    global product
    tipo = input("¿Que clase de producto va a ingresar?\t1.botana\t2.bebida\t3.dulce: ")
    if int(tipo) == 1 or int(tipo) == 2 or int(tipo) == 3:
        marca = input("Ingrese el nombre del producto: ")
        cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
        precio = int(input("Ingrese el  precio del producto: "))
        if int(tipo) == 1:
            tipo = "Botana"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            sabor = input("Ingrese el sabor del producto: ")
        elif int(tipo) == 2:
            tipo = "Bebida"
            gramos = int(input("Ingrese los mililitros que contiene el producto: "))
            sabor = input("Ingrese el sabor del producto: ")
        else:
            tipo = "Dulces"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            sabor = []
            while 1:
                sabor.append(input("Ingrese el sabor del producto: "))
                anadir=input("¿Desea ingresar otro sabor?\n1.Si\n2.No\n")
                if int(anadir) == 1:
                    continue
                elif int(anadir) == 2:
                    break
                else:
                    print("Ingrese un valor valido")
    else:
        print("ingrese valores validos")
        return 0
    with open("productos.csv", "r") as f:
        for linea in f.readlines():
            linea.split(",")

        clave=int(linea[0])+1
    with open('productos.csv', 'a+') as f:
        f.write(f"\n{clave},{marca},{cantidad},{precio},{sabor},{gramos},{tipo}")

def eliminarProducto(lista):
    clave = int(input('ingrese la clave del producto que desea eliminar'))
    lista.pop(clave-1)
    for i in range(len(lista)):
        lista[i].clave = i+1
    actualizarDatos(lista)

def crearAdmin():
    nombre = input("Ingrese el nombre del nuevo administrador: ")
    contraseña = input("Ingrese su contraseña: ")
    nuevoAdmin = Administrador(nombre, contraseña)
    nuevoAdmin.nuevoAdmin()

def iniciarSesion(lista):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    admin = Administrador(usuario, contraseña)
    validar = admin.validacion()
    print("\n")
    if validar == 1:
        opcion = int(input(f"Bienvenido {usuario}. ¿Que desea hacer?\n\n\
1. Añadir producto\n\
2. Eliminar producto\n\
3. Modificar información de un producto\n\
4 Crear nuevo administador\n\
5. Cerrar Sesión (Volver al menú inicial)\n\
6. Salir\n"))
        print("\n")
        if opcion == 1:
            añadirProducto()
        elif opcion == 2:
            eliminarProducto(lista)
        elif opcion == 4:
            crearAdmin()
        elif opcion == 5:
            #main()
            print("ola")
    else:
        print("Contraseña o usuario erroneos")

