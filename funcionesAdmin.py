from productos import *
from admin import Administrador
from Proyecto import main

product = []

def añadirProducto():
    global product
    with open("productos.csv", "r") as f:
        for clave in f.readlines:
            claveNueva = clave[0]
  
    with open('productos.csv', 'a+') as f:
        print()

def crearAdmin():
    nombre = input("Ingrese el nombre del nuevo administrador: ")
    contraseña = input("Ingrese su contraseña: ")
    nuevoAdmin = Administrador(nombre, contraseña)
    nuevoAdmin.nuevoAdmin()

def iniciarSesion():
    if not admin:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        admin = Administrador(usuario, contraseña)
        validar = admin.validacion()
    if validar == 1:
        opcion = int(input(f"Bienvenido {usuario}. ¿Que desea hacer?\n\n\
1. Añadir producto\n\
2. Eliminar producto\n\
3. Modificar información de un producto\n\
4 Crear nuevo administador\n\
5. Volver al menú inicial\n\
6. Salir\n"))
        print("\n")
        if opcion == 1:
            añadirProducto()
        elif opcion == 4:
            crearAdmin()
        elif opcion == 5:
            main()
    else:
        print("Contraseña o usuario erroneos")

