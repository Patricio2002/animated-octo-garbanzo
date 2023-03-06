from admin import *
from funcionesAdmin import *
import time
maquina = MaquinaExpendedora()
from excepciones import *

def dispensando() -> str: 
    """
    Esta función simula el momento en que se dispensa el producto.
    """ 

    print("Dispensando...")
    
    for i in range(1, 5):
        time.sleep(0.5)
    
    print()
    print("Recoja su producto, gracias por comprar :)\n")

        

def seleccionarProducto(lista: list) -> None: #le resta uno a la cantidad que se tiene de un producto para simular la compra
    """
     Esta función simula la compra del producto, restando una unidad a la cantidad de productos\n
     que se encuentren en el archivo "productos.csv". Esto se puede ver visualmente.
    """ 
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
        if(int(lista[clave].cantidad)>0):
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
        else:
            print('Producto sin existencia')
            
def productosTipo(lista: list) -> str:
    """
      Esta función muestra los productos de un solo tipo, sean Bebidas, Botanas o Dulces.
    """ 
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

def infoProducto(lista: list) -> str: #muestra la información de un solo producto
    """
      Esta función muestra la información del producto que se requiera saber.
    """ 
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
    """
     Esta es la función principal.
        """  
    while 1:
        lista = maquina.mostrarProductos()
        try: 
            opcion = int(input("¿Qué es lo que desea hacer?\n\
  1. Seleccionar producto\n\
  2. Mirar productos por tipo\n\
  3. Ver informacion de un producto\n\
  4. Modo Administrador\n\
  5. Salir\n"))
        except ValueError:          #verifica que solo ingresen números
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