from productos import *
from admin import Administrador

maquina = MaquinaExpendedora()
product = []

#Esta función extrae el valor de los atributos de la clase lista y los actualiza en el csv
def actualizarDatos(lista):
    act = []
    for i in range(len(lista)):
        act.append(lista[i].retornarInfo())
    maquina.actualizarCSV(act)

#función que lee todos los datos nuevos del producto y lo sube al csv
def añadirProducto():
    global product
    tipo = input("¿Que clase de producto va a ingresar?\t1.botana\t2.bebida\t3.dulce: ")
    if int(tipo) == 1 or int(tipo) == 2 or int(tipo) == 3:
        marca = input("Ingrese el nombre del producto: ")
        cantidad= int(input("Ingrese la cantidad de unidades del producto: "))
        precio = int(input("Ingrese el  precio del producto: "))
        if int(tipo) == 1:
            tipo = "Botana"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            sabor = input("Ingrese el sabor del producto: ")
        elif int(tipo) == 2:
            tipo = "Bebida"
            gramos = int(input("Ingrese los mililitros que contiene el producto: "))
            sabor = input("Ingrese el sabor del producto: ")
        else:
            tipo = "Dulces"
            gramos = int(input("Ingrese la cantidad de  gramos que contiene el producto: "))
            sabor = (input("Ingrese el sabor del producto: "))
            while 1:
                sabor2 = ''
                anadir=input("¿Desea ingresar otro sabor?\n1.Si\n2.No\n")
                if int(anadir) == 1:
                    sabor = (input("Ingrese el sabor del producto: "))
                    sabor2 = anadir + ". " + sabor
                elif int(anadir) == 2:
                    sabor = sabor2
                    break
                else:
                    print("Ingrese un valor valido")
    else:
        print("ingrese valores validos")
        return 0
    with open("productos.csv", "r") as f:
        for linea in f.readlines():
            linea.split(",")

        clave=int(linea[0])+1
    with open('productos.csv', 'a+') as f:
        f.write(f"{clave},{marca},{cantidad},{precio},{sabor},{gramos},{tipo}")

#función que modifica un valor de un atributo y lo envía a la función actualizarDatos
def modificarProducto(lista):
    try:
        clave = int(input('ingrese la clave del producto que desea modificar'))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        clave = clave-1
        modif = int(input('ingrese el dato que desee cambiar:\n\
    1. nombre\n2. costo\n3. cantidad\n4. gramos\n5. sabor\n'))
        if modif == 1:
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            lista[clave].nombre = nuevoNombre
        elif modif == 2:
            nuevoCosto = int(input("Ingrese el nuevo costo: "))
            lista[clave].costo = nuevoCosto
        elif modif == 3:
            nuevaCantidad = int(input("Ingrese cuantas unidades del producto va a agregar: "))
            lista[clave].cantidad = nuevaCantidad
        elif modif == 4:
            nuevoGramo = int(input("Ingrese la nueva cantidad de contenido que trae el producto: "))
            if(lista[clave]._tipo == 'Bebida'):
                lista[clave].mililitros = nuevoGramo
            else:
                lista[clave].gramos = nuevoGramo
        elif modif == 5:
            nuevoSabor = int(input("Ingrese el nuevo sabor del producto: "))
            lista[clave].sabor = nuevoSabor
        actualizarDatos(lista)
        
#función que elimina un producto de lista para luego actualizarlo
def eliminarProducto(lista):
    try: 
        clave = int(input('ingrese la clave del producto que desea eliminar'))
    except ValueError: 
            print("\nIntroduzca solo numeros!!!")
    else:
        lista.pop(clave-1)
        for i in range(len(lista)):
            lista[i].clave = i+1
        actualizarDatos(lista)

#función que genera un nuevo admin en administradores.csv
def crearAdmin():
    nombre = input("Ingrese el nombre del nuevo administrador: ")
    contraseña = input("Ingrese su contraseña: ")
    if len(nombre) != 0 or len(contraseña) != 0:
        nuevoAdmin = Administrador(nombre, contraseña)
        nuevoAdmin.nuevoAdmin()

#función que valida si existe la cuenta y contraseña del admin que desea ingresar
def iniciarSesion(lista):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    admin = Administrador(usuario, contraseña)
    validar = admin.validacion()
    print("\n")
    #en caso de que exista, se despliega el menú del admin
    if validar == 1:
        while(1):
            try:
                opcion = int(input(f"Bienvenido {usuario}. ¿Que desea hacer?\n\n\
1. Añadir producto\n\
2. Eliminar producto\n\
3. Modificar información de un producto\n\
4 Crear nuevo administador\n\
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

