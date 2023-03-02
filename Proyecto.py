from admin import *
from funcionesAdmin import *
from funcionesAdmin import iniciarSesion
import time
maquina = MaquinaExpendedora()


def dispensando():

    print("Dispensando...")
    
    for i in range(1, 10):
        #print("[" + "|" * i + "]")
        time.sleep(0.5)
        
    #
    print()
    print("Recoja su producto, gracias por comprar :)")

        
def mostrarProductos():
    pass

def seleccionarProducto():
    clave = input("Ingrese la clave del producto que desea comprar: ")
    maquina.comprarProductos(int(clave))
    dispensando()

def productosTipo():
    pass

def infoProductos():
    pass

    #if validar:
    #   print(f"Bienvenido {usuario}")
 

def main():
    while 1:
        maquina.mostrarProductos()
        try:
            opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Ver informacion de un producto\n\
  3. Modo Administrador\n\
  4. Salir\n"
  ":"))
            if opcion == 1:
                seleccionarProducto()
            elif opcion == 3:
                iniciarSesion()
            elif opcion == 4:
                print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
            break
       
        except ValueError:
        
         print("\nIntroduzca solo numeros!!!")


main()
