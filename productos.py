
listaClases = []


class MaquinaExpendedora():
    """
    Esta clase se encarga de construir un objeto de tipo Maquina Expendedora.
    """
    def __init__(self) -> None:
        pass
    
    def mostrarProductos(self) -> str:
        """
        Creado el objeto de tipo maquina expendedora, este método se encarga \n
        de mostrar los productos contenidos en la máquina expendedora.
        """
        lista = []
        print("\n\t-Maquina expendedora krunkito-\n")
        with open('productos.csv', 'r') as f:
            i=1
            for linea in f.readlines():
                linea2 = linea.split(",")
                if int(linea2[2]) > 0:
                    print(f"{linea2[0]}.{linea2[1]}: ${linea2[3]}", end="   ")
                else:
                    print(f'{linea2[0]}.sin existencias', end="   ")
                if i%3 == 0:
                    print("\n")
                clase = linea2[6].rstrip('\n')
                
                lista.append(globals()[clase](linea2[0], linea2[1], linea2[2], linea2[3],linea2[4],linea2[5]))
                i+=1

        print("\n")
        return lista  
    

    def actualizarCSV(self, lista: list) -> None:
        """
        El método actualiza los datos del archivo ".csv" según los introducidos.
        """
        with open('productos.csv', "w") as f:
            for i in lista:
                f.write(f"{i}\n")
    
class Producto():          
    """
    Esta es la clase padre para los productos, de la que heredarán atributos y métodos los objetos de tipo Producto.
    """                
    def __init__(self,clave,  nombre, cantidad, costo):
        self.clave = clave
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        
    def  infoGeneral(self) -> str:
        """
        El método muestra los atributos del objeto.
        """                 
        print(f"clave: {self.clave}\n\
nombre: {self.nombre}\n\
costo: {self.costo}\n\
cantidad en existencia:{self.cantidad}")
    def añadirProductoGen(self) -> None:
        """
        Este método añade prodcutos del tipo que se refiera. Por ejemplo:\n
        Botanas, Bebidas, etc.
        """
        with open('productos.csv', 'a+') as f:
            f.write(f"\n{self.clave},{self.nombre},{self.cantidad},{self.costo}")
    
    def retornarPrecio(self):
        """
        Este método retorna el precio del producto.
        """
        return int(self.costo)
    
    def comprar(self):
        """
        Este método resta un producto a la cantidad que yace en la máquina, una vez sea comprado.
        """
        self.cantidad = int(self.cantidad)-1
    
class Botana(Producto):   
    """
    Clase que crea productos de tipo "Botana". Hereda de la clase Producto.
    """       
    def __init__(self,clave, nombre, cantidad, costo ,sabor, gramos, tipo = "Botana"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              
        self.gramos = gramos
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)
    

    def infoEspecifica(self) -> None:
        """
        Este método muestra la información específica del producto.
        """
        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
gramos: {self.gramos}")
        
    def añadirProducto(self) -> None:
        """
        Este método añade productos de tipo "Botana".
        """
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self._tipo}")

    def retornarInfo(self) -> str:
        """
    Este método muestra la información requerida del producto.
    """   
        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabor},{self.gramos},{self._tipo}"

class Bebida(Producto): 
    """
    Clase que crea productos de tipo "Bebida". Hereda de la clase Producto.
    """            
    def __init__(self,clave, nombre, cantidad, costo ,sabor, mililitros,  tipo = "Bebida"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              
        self.mililitros = mililitros
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)

    def infoEspecifica(self) -> str:
        """
        Este método muestra la información específica del producto.
        """

        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
mililitros: {self.mililitros}")
        
    def añadirProducto(self) -> None:
        """
        Este método añade productos de tipo "Bebida".
        """
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabor},{self.gramos},{self.tipo}")
    def retornarInfo(self) -> str:
        """
         Este método muestra la información requerida del producto.
        """ 
        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabor},{self.mililitros},{self._tipo}"
        

class Dulces(Producto):    
    """
    Clase que crea productos de tipo "Dulces". Hereda de la clase Producto.
    """         
    def __init__(self,clave, nombre, cantidad, costo , sabores ,gramos, tipo = "Dulces"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo                  
        self.sabores = sabores
        self.gramos =  gramos
        self._tipo = tipo

        super().__init__(clave, nombre, cantidad, costo)

    def infoEspecifica(self) -> None:
        """
        Este método muestra la información específica del producto.
        """
        print(f"clave: {self.clave}\n\
producto: {self._tipo}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor(es): {self.sabores}\n\
gramos: {self.gramos}")

    def añadirProducto(self) -> None:
        """
        Este método añade productos de tipo "Dulces".
        """
        self.añadirProductoGen()
        with open('productos.csv', 'a+') as f:
            f.write(f",{self.sabores},{self.gramos},{self._tipo}")

    def retornarInfo(self) -> str:
        """
        Este método muestra la información requerida del producto.
        """ 
        return f"{self.clave},{self.nombre},{self.cantidad},{self.costo},{self.sabores},{self.gramos},{self._tipo}"