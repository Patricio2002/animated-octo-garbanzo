from admin import *
from funcionesAdmin import *
from productos import *
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
    while 1:
        opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Enlistar total de productos de un tipo\n\
  3. Enlistar todos los productos\n\
  4. Ver informacion de un producto\n\
  5. Modo administrador\n\
  6. Salir\n"))
     
        if opcion == 1:
            pass

        if opcion == 5:         #cambiar 
            print("Inicie sesión: ")
            iniciarSesion()


                
        elif opcion == 6:
            print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
            break

main()
