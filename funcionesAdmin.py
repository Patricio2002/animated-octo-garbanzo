from productos import *

product = []

def añadirProducto():
    global product
    with open("productos.csv", "r") as f:
        for clave in f.readlines:
            claveNueva = clave[0]
  
    with open('productos.csv', 'a+') as f:
        print()
