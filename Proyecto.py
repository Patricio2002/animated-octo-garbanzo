from admin import *
from funcionesAdmin import *
from funcionesAdmin import iniciarSesion
import time
maquina = MaquinaExpendedora()
from excepciones import *

def dispensando():

    print("Dispensando...")
    
    for i in range(1, 5):
        time.sleep(0.5)
        
    
    print()
    print("Recoja su producto, gracias por comprar :)\n")

#Comentar todas las clases, funciones y métodos
        
def monto(dinero, clave):
    

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
        monto = int(input(("Introduzca el monto: ")))       #Se verifica la cantidad del monto
        if lista[clave].retornarPrecio() == monto:
            lista[clave].comprar()
            actualizarDatos(lista)
            dispensando()            
        elif monto > lista[clave].retornarPrecio(): #Si excede, regresa el cambio
            print("Su cambio: " + str(monto - lista[clave].retornarPrecio()))
            lista[clave].comprar()
            actualizarDatos(lista)
            dispensando() 
        elif monto < lista[clave].retornarPrecio():
            print("Monto insuficiente :(")
            print()
            
       


def productosTipo():        #Mostrar tipo de productos por tipo

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

 

def main():     #Verificar que se ingrese el monto, monto correcto de cambio y regreso de cambio en el caso
    lista = maquina.mostrarProductos()   
    while 1:
        try: 
            opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Mirar productos por tipo\n\
  3. Ver informacion de un producto\n\
  4. Modo Administrador\n\
  5. Salir\n"))
        except ValueError:          #Quinta opcion para mostrar productos por tipo
            print("\nIntroduzca solo numeros!!!\n")
        else:    
            if opcion == 1:
                seleccionarProducto(lista)
            elif opcion == 2:
                
             maquina.productoBotana()
                
            elif opcion == 3:
                infoProducto(lista)
            elif opcion == 4:
                iniciarSesion(lista)
            elif opcion == 5:
                print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
                break


main()

