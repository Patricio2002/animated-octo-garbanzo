from admin import *
from funcionesAdmin import *
from funcionesAdmin import iniciarSesion
#from productos import *
maquina = MaquinaExpendedora()

def seleccionarProducto(lista):
    clave = input("Ingrese la clave del producto que desea comprar: ")
    clave = int(clave)-1
    if(clave < len(lista)):
        print(lista[clave].cantidad)
        lista[clave].comprar()
        print(lista[clave].cantidad)
    else:
        print('No se reconoce esa clave')

def productosTipo():
    pass

def infoProducto(lista):
    clave = input("Ingrese la clave del producto del que desa saber mas información: ")
    clave = int(clave)-1
    if(clave < len(lista)):
        print(lista[clave].infoEspecifica())
    else:
        print('No se reconoce esa clave')
 

def main():
    while 1:
        lista = maquina.mostrarProductos()
        #maquina.mostrarProductos()
        opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Ver informacion de un producto\n\
  3. Modo Administrador\n\
  4. Salir\n"))
        if opcion == 1:
            seleccionarProducto(lista)
        elif opcion == 2:
            infoProducto(lista)
        elif opcion == 3:
            iniciarSesion()
        elif opcion == 4:
            print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
            break

main()
