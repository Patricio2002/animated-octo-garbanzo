from productos import *
from admin import Administrador

maquina = MaquinaExpendedora()
product = []

def validarCantidades (cantidades):
    if cantidades<=0:
        print("Ingrese cantidad valida")
        return False
    else:
        return True

def actualizarDatos(lista):
    act = []
    for i in range(len(lista)):
        act.append(lista[i].retornarInfo())
    maquina.actualizarCSV(act)

def añadirProducto():
    global product
    tipo = input("¿Qué clase de producto va a ingresar?\t1.Botana\t2.Bebida\t3.Dulce: \n")
    if int(tipo) == 1 or int(tipo) == 2 or int(tipo) == 3:

        marca = input("Ingrese el nombre del producto: ")

        cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
        while validarCantidades(cantidad)==False:
             cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
             continue

        precio = int(input("Ingrese el  precio del producto: "))
        while validarCantidades(cantidad)==False:
             cantidad= int(input("Ingrese el precio del producto: "))
             continue
        
        if int(tipo) == 1:
            tipo = "Botana"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            while validarCantidades(cantidad)==False:
             cantidad= int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
             continue
            sabor = input("Ingrese el sabor del producto: ")

        elif int(tipo) == 2:
            tipo = "Bebida"
            gramos = int(input("Ingrese los mililitros que contiene el producto: "))
            while validarCantidades(cantidad)==False:
             cantidad= int(input("Ingrese los mililitros que contiene el producto: "))
             continue 
            sabor = input("Ingrese el sabor del producto: ")

        else:
            tipo = "Dulces"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            while validarCantidades(cantidad)==False:
             cantidad= int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
             continue
            sabor = (input("Ingrese el sabor del producto: "))
            while 1:
                añadir=input("¿Desea ingresar otro sabor?\n1.Si\n2.No\n")
                if int(añadir) == 1:
                    añadir = añadir + ". " +(input("Ingrese el sabor del producto: "))
                elif int(añadir) == 2:
                    break
                else:
                    print("Ingrese un valor valido")

    else:
        print("Ingrese valores validos")
        return 0
    
    with open("productos.csv", "r") as f:
        for linea in f.readlines():
            linea.split(",")
        clave=int(linea[0])+1
    with open('productos.csv', 'a+') as f:
        f.write(f"\n{clave},{marca},{cantidad},{precio},{sabor},{gramos},{tipo}")

def modificarProducto(lista):
    try:
        clave = int(input('Ingrese la clave del producto que desea modificar'))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        clave = clave-1
        modif = int(input('ingrese el dato que desee cambiar:\n\
    1. Nombre\n2. Costo\n3. Cantidad\n4. Gramos\n5. Sabor\n'))
        
        if modif == 1:
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            lista[clave].nombre = nuevoNombre

        elif modif == 2:
            nuevoCosto = int(input("Ingrese el nuevo costo: "))
            while validarCantidades(nuevoCosto)==False:
             nuevoCosto= int(input("Ingrese el nuevo costo: "))
             continue
            lista[clave].costo = nuevoCosto

        elif modif == 3:
            nuevaCantidad = int(input("Ingrese cuantas unidades del producto va a agregar: "))
            while validarCantidades(nuevaCantidad)==False:
             nuevaCantidad= int(input("Ingrese cuantas unidades del producto va a agregar: "))
             continue
            lista[clave].cantidad = nuevaCantidad

        elif modif == 4:
            nuevoGramo = int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
            if(lista[clave]._tipo == 'Bebida'):
                while validarCantidades(nuevoGramo)==False:
                 nuevoGramo= int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
                 continue
                lista[clave].mililitros = nuevoGramo
            else:
                while validarCantidades(nuevoGramo)==False:
                 nuevoGramo= int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
                 continue
                lista[clave].gramos = nuevoGramo

        elif modif == 5:
            nuevoSabor = int(input("Ingrese el nuevo sabor del producto: "))
            lista[clave].sabor = nuevoSabor

        actualizarDatos(lista)
        
def eliminarProducto(lista):
    try: 
        clave = int(input('Ingrese la clave del producto que desea eliminar'))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        while validarCantidades(clave)==False or clave>=len(lista)+2:
                 clave= int(input("Ingrese clave existente: "))
                 continue
        lista.pop(clave-1)
        for i in range(len(lista)):
            lista[i].clave = i+1
        actualizarDatos(lista)

def crearAdmin():
    nombre = input("Ingrese el nombre del nuevo administrador: ")
    contraseña = input("Ingrese su contraseña: ")
    if len(nombre) != 0 or len(contraseña) != 0:
        nuevoAdmin = Administrador(nombre, contraseña)
        nuevoAdmin.nuevoAdmin()

def iniciarSesion(lista):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    admin = Administrador(usuario, contraseña)
    validar = admin.validacion()
    print("\n")
    if validar == 1:
        while(1):
            try:
                opcion = int(input(f"Bienvenido {usuario}. \n¿Qué desea hacer?\n\n\
1. Añadir producto\n\
2. Eliminar producto\n\
3. Modificar información de un producto\n\
4. Crear nuevo administador\n\
5. Cerrar Sesión (Volver al menú inicial)\n"))
                print("\n")
            except ValueError: 
                print("\nIntroduzca solo numeros!!!")
            else:
                if opcion == 1:
                    añadirProducto()
                elif opcion == 2:
                    eliminarProducto(lista)
                elif opcion == 3:
                    modificarProducto(lista)
                elif opcion == 4:
                    crearAdmin()
                elif opcion == 5:
                    break
                else:
                    print('Ingrese valores validos')
    else:
        print("Contraseña o usuario erroneos")