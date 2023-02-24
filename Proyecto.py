from admin import Administrador
from productos import *

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
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    Administrador(usuario, contraseña)

    validar = Administrador.validacion()

    if validar:
        print(f"Bienvenido {usuario}")
        opcion = input("¿Que desea hacer?\n\
1. Añadir nuevo producto\n\
2. Eliminar producto\n\
3. Modificar informaciónd de un producto\n\
4. Cerrar sesión")
 

def main():
    opcion = int(input("¿Qué es lo que desea hacer?\n\
1. Seleccionar producto\n\
3. Enlistar total de productos de un tipo\n\
4. Enlistar todos los productos\n\
5. Ver informacion de un producto\n\
2. Iniciar sesión (Administrador)\n\
    "))