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
 

def main():
    opcion = int(input("¿Qué es lo que desea hacer?\n\
1. Seleccionar producto\n\
2. Almacenar nuevo producto\n\
3. Enlistar total de productos de un tipo\n\
4. Enlistar todos los productos\n\
5. Ver informacion de un producto\n\
    "))