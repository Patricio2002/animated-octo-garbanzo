from admin import *
from funcionesAdmin import *
#from productos import *
validar = 0

productos =  {}
f = open('productos.csv', "r")

def mostrarProductos():
    pass

def seleccionarProducto():
    pass

def productosTipo():
    pass

def infoProductos():
    pass

def iniciarSesion():
    global validar
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
5. Salir\n"))
        print("\n")
        if opcion == 1:
            añadirProducto()
    else:
        print("Contraseña o usuario erroneos")



    #if validar:
    #   print(f"Bienvenido {usuario}")
 

def main(): 
    opcion = int(input("¿Qué es lo que desea hacer?\n\
1. Seleccionar producto\n\
2. Enlistar total de productos de un tipo\n\
3. Enlistar todos los productos\n\
4. Ver informacion de un producto\n\
5. Iniciar sesion: Administrador\n\
6. Salir\n"))
    if opcion == 5:
        iniciarSesion()

main()