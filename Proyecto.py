from admin import *
from funcionesAdmin import *
import time
maquina = MaquinaExpendedora()
from excepciones import *

def dispensando(): #envia mensajito al comprar el producto

    print("Dispensando...")
    
    for i in range(1, 5):
        time.sleep(0.5)
        
    
    print()
    print("Recoja su producto, gracias por comprar :)\n")

#Comentar todas las clases, funciones y métodos
        

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
             productosTipo(lista)
            elif opcion == 3:
                infoProducto(lista)
            elif opcion == 4:
                iniciarSesion(lista)
            elif opcion == 5:
                print("Gracias por haber utilizado la maquina expendedora 'Kunkito'")
                break

main()