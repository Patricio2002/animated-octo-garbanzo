#Ideas jeje
class Producto():                           #Clase padre
    def __init__(self,clave,  marca, cantidad, costo, producto):
        self.clave = clave
        self.producto = producto
        self.marca = marca
        self.costo = costo
        self.cantidad = cantidad
        
    def  infoGeneral(self):
        print(f"producto: {self.producto}\nmarca: {self.marca}\ncantidad en existencia:{self.cantidad}")
    

class Botanas(Producto):          
    def __init__(self,clave, marca, cantidad, costo ,sabor, gramos, tipo = "botana"):
        self.clave = clave
        self.marca = marca
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor
        self.gramos = gramos
        self._tipo = tipo

        super().__init__()

class bebida(Producto):          
    def __init__(self,clave, marca, cantidad, costo ,sabor, mililitros,  tipo = "bebida"):
        self.clave = clave
        self.marca = marca
        self.cantidad = cantidad
        self.costo = costo
        self.sabor = sabor
        self.mililitros = mililitros
        self._tipo = tipo

        super().__init__()

class Dulces(Producto):          
    def __init__(self,clave, marca, cantidad, costo , sabores ,gramos, tipo = "dulces"):
        self.clave = clave
        self.marca = marca
        self.cantidad = cantidad
        self.costo = costo
        self.sabores = sabores
        self.gramos =  gramos
        self._tipo = tipo

        super().__init__()
