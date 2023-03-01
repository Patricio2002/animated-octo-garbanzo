#Ideas jeje
class Producto():                           #Clase padre
    def __init__(self,clave,  nombre, cantidad, costo, producto):
        self.clave = clave                      #Se inicializan los atributos del objeto
        self.producto = producto
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        
    def  infoGeneral(self):                 #Se muestran los atributos del objeto
        print(f"clave: {self.clave}\n\
producto: {self.producto}\n\
nombre: {self.nombre}\n\
costo: {self.costo}\n\
cantidad en existencia:{self.cantidad}")


#Clases hijas

class Botanas(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, gramos, tipo = "botana"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              #Atributos de la clase Botana
        self.gramos = gramos
        self._tipo = tipo

        super().__init__()
    

    def infoEspecifica(self) -> None:
        print(f"clave: {self.clave}\n\
producto: {self.producto}\n\
nombre: {self.nombre}\n\
cantidad en existencia:{self.cantidad}\n\
costo:{self.costo}\n\
sabor: {self.sabor}\n\
gramos: {self.gramos}")     #Se muestran atributos

class bebida(Producto):          
    def __init__(self,clave, nombre, cantidad, costo ,sabor, mililitros,  tipo = "bebida"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor              #Atributos de la clase bebida
        self.mililitros = mililitros
        self._tipo = tipo

        super().__init__()

class Dulces(Producto):          
    def __init__(self,clave, nombre, cantidad, costo , sabores ,gramos, tipo = "dulce"):
        self.clave = clave
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo                  #Atributos de la clase dulce
        self.sabores = sabores
        self.gramos =  gramos
        self._tipo = tipo

        super().__init__()
