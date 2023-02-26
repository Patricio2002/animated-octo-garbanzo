#Ideas jeje
class Producto():                           #Clase padre
    def __init__(self,clave,  marca, cantidad, costo, producto):
        self.clave = clave
        self.producto = producto
        self.marca = marca
        self.costo = costo
        self.cantidad = cantidad
        
    def  revisarInfo(self):
        print(f"producto: {self.producto}\nmarca: {self.marca}\ncantidad en existencia:{self.cantidad}")

class Papas(Producto):          
    def __init__(self,clave, marca, cantidad, costo , tipo = "papas"):
        self.clave = clave
        self.marca = marca
        self.cantidad = cantidad
        self.costo = costo
        self._tipo = tipo

        super().__init__()


#class MaquinaExpendedora():     #Clase principal
 #   elemento = Producto("Papas", "Sabritas")
  #  def __init__(elemento):
    #    pass