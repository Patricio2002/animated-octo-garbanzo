from admin import *
from funcionesAdmin import *
from funcionesAdmin import iniciarSesion
import time
maquina = MaquinaExpendedora()
from excepciones import *

def dispensando():

    print("Dispensando...")
    
    for i in range(1, 5):
        #print("[" + "|" * i + "]")
        time.sleep(0.5)
        
    #
    print()
    print("Recoja su producto, gracias por comprar :)\n")

        
def mostrarProductos():
    pass

def seleccionarProducto(lista):
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


def productosTipo():
    pass

def infoProducto(lista):
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
  3. Modo Administrador\n\
  4. Salir\n"))
        except ValueError: 
            print("\nIntroduzca solo numeros!!!\n")
        else:    
            if opcion == 1:
                seleccionarProducto(lista)
            elif opcion == 2:
                infoProducto(lista)
            elif opcion == 3:
                iniciarSesion(lista)
            elif opcion == 4:
                print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
                break


main()

