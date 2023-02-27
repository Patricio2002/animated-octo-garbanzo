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