from admin import *
from funcionesAdmin import *
from funcionesAdmin import iniciarSesion
import time
maquina = MaquinaExpendedora()
from excepciones import *

def dispensando(): #envia mensajito al comprar el producto

    print("Dispensando...")
    
    for i in range(1, 5):
        #print("[" + "|" * i + "]")
        time.sleep(0.5)
        
    #
    print()
    print("Recoja su producto, gracias por comprar :)\n")

        
def mostrarProductos():
    pass

def seleccionarProducto(lista): #le resta uno a la cantidad que se tiene de un producto para simular la compra
    try:
        clave = int(input("Ingrese la clave del producto que desea comprar: "))
        verifClave(lista,clave)
    except ValueError: 
            print("\nIntroduzca solo numeros!!!\n")
    except ClaveDesconocida :
        print("\nIngrese una clave conocida\n")
    except IndexError:
        print("\nIngrese una clave conocida\n")
    else: 
        clave = int(clave)-1
        lista[clave].comprar()
        actualizarDatos(lista)
        dispensando()


def productosTipo(lista):
    try:
        tipo = int(input('Ingrese el tipo de productos que desee ver: \n1. Botanas\n2. Bebida\n3. Dulces\n'))
        if tipo == 1:
            for i in range(len(lista)):
                if lista[i]._tipo == 'Botana':
                    print(lista[i].infoGeneral())
        elif tipo == 2:
            for i in range(len(lista)):
                if lista[i]._tipo == 'Bebida':
                    print(lista[i].infoGeneral())
        elif tipo == 3:
            for i in range(len(lista)):
                if lista[i]._tipo == 'Dulces':
                    print(lista[i].infoGeneral())
    except ValueError:
        print("Ingrese solo valores válidos")  

def infoProducto(lista): #muestra la información de un solo producto
    try:
        clave = int(input("Ingrese la clave del producto del que desa saber mas información: "))
        verifClave(lista,clave)
    except ValueError: 
            print("\nIntroduzca solo numeros!!!\n")
    except ClaveDesconocida :
        print("\nIngrese una clave conocida\n")
    except IndexError:
        print("\nIngrese una clave conocida\n")
    else:
        clave = int(clave)-1
        info = lista[clave].infoEspecifica()
        print(info)

 

def main():
    lista = maquina.mostrarProductos()   
    while 1:
        try: 
            opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Ver informacion de un producto\n\
  3. Ver todos los los productos de un tipo\n\
  4. Modo Administrador\n\
  5. Salir\n"))
        except ValueError: 
            print("\nIntroduzca solo numeros!!!\n")
        else:    
            if opcion == 1:
                seleccionarProducto(lista)
            elif opcion == 2:
                infoProducto(lista)
            elif opcion == 3:
                productosTipo(lista)
            elif opcion == 4:
                iniciarSesion(lista)
            elif opcion == 5:
                print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
                break


main()

