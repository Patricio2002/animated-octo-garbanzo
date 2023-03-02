#Ideas jeje
class MaquinaExpendedora():
    def __init__(self) -> None:
        pass
    def mostrarProductos(self):
        print("\n\t-Maquina expendedora krunkito-\n\n")
        with open('productos.csv', 'r') as f:
            i=0
            for linea in f.readlines():
                i+=1
                linea2 = linea.split(",")
                print(f"   {linea2[0]}-{linea2[1]}:{linea2[4]}. ${linea2[3]}", end='')
                if i%3 == 0:
                    print("")
        print("\n\n")
    
    def comprarProductos(self, clave):
        todos = []
        with open('productos.csv', 'r') as f:
            for linea in f.readlines():
                linea2 = linea.split(',')
                if clave  == int(linea2[0]):
                    linea2[2] = int(linea2[2])-1
                
                todos.append(linea2)
        with open('productos.csv','w') as f:
            for item in todos:
                for i in range(len(item)):
                    f.write(f"{str(item[i])}")
                    if(i<len(item)-1):
                        f.write(',')
                #f.write('\n')

            
                          
    
class Producto():                           #Clase padre
    def __init__(self,clave,  nombre, cantidad, costo):
        self.clave = clave
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        
    def infoGeneral(self):                 #Se muestran los atributos del objeto
        print(f"clave: {self.clave}\n\
nombre: {self.nombre}\n\
costo: {self.costo}\n\
cantidad en existencia:{self.cantidad}")
    def añadirProductoGen(self):
        with open('productos.csv', 'a+') as f:
            f.write(f"\n{self.clave},{self.nombre},{self.cantidad},{self.costo}")
    
class Botanas(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, gramos, tipo = "botana"):
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
producto: {self.producto}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
gramos: {self.gramos}")
        
    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self._tipo}")

class bebida(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, mililitros,  tipo = "bebida"):
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
producto: {self.producto}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
mililitros: {self.mililitros}")
        
    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self.tipo}")

class Dulces(Producto):          
    def __init__(self,clave, nombre, cantidad, costo , sabores ,gramos, tipo = "dulce"):
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
producto: {self.producto}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor(es): {self.sabor}\n\
gramos: {self.gramos}")

    def añadirProducto(self):
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self._tipo}")