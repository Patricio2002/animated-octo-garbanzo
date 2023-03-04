#Ideas jeje
listaClases = []


class MaquinaExpendedora():
    def __init__(self) -> None:
        pass
    def mostrarProductos(self):
        lista = []
        print("\n\t-Maquina expendedora krunkito-\n")
        with open('productos.csv', 'r') as f:
            i=1
            for linea in f.readlines():
                
                linea2 = linea.split(",")
                print(f"{linea2[0]}.{linea2[1]}: ${linea2[3]}", end="   ")
                if i%3 == 0:
                    print("\n")
                clase = linea2[6].rstrip('\n')
                lista.append(globals()[clase](linea2[0], linea2[1], linea2[2], linea2[3],linea2[4],linea2[5]))
                i+=1

        print("\n\n")
        return lista  
    def actualizarCSV(self, lista):
        with open('productos.csv', "w") as f:
            for i in lista:
                f.write(f"{i}\n")
    
class Producto():                           #Clase padre
    def __init__(self,clave,  nombre, cantidad, costo):
        self.clave = clave
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        
    def  infoGeneral(self):                 #Se muestran los atributos del objeto
        print(f"clave: {self.clave}\n\
nombre: {self.nombre}\n\
costo: {self.costo}\n\
cantidad en existencia:{self.cantidad}")
    def añadirProductoGen(self):
        with open('productos.csv', 'a+') as f:
            f.write(f"\n{self.clave},{self.nombre},{self.cantidad},{self.costo}")
    
    def retornarInfo(self):
        pass
    
    def comprar(self):
        self.cantidad = int(self.cantidad)-1
    
class Botana(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, gramos, tipo = "Botana"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              #Atributos de la clase Botana
        self.gramos = gramos
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)
    

    def infoEspecifica(self) -> None:
        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
gramos: {self.gramos}")
        
    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self._tipo}")

    def retornarInfo(self):
        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabor},{self.gramos},{self._tipo}"

class Bebida(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, mililitros,  tipo = "Bebida"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              #Atributos de la clase bebida
        self.mililitros = mililitros
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)

    def infoEspecifica(self):
        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
mililitros: {self.mililitros}")
        
    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self.tipo}")
    def retornarInfo(self):

        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabor},{self.mililitros},{self._tipo}"
        

class Dulces(Producto):          
    def __init__(self,clave, nombre, cantidad, costo , sabores ,gramos, tipo = "Dulces"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo                  #Atributos de la clase dulce
        self.sabores = sabores
        self.gramos =  gramos
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)

    def infoEspecifica(self):
        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor(es): {self.sabor}\n\
gramos: {self.gramos}")

    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self._tipo}")

    def retornarInfo(self):
        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabor},{self.gramos},{self._tipo}"