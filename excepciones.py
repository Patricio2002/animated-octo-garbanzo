class ClaveDesconocida(Exception):
    """
    Esta clase se encarga de manejar las expeciones que puedan presentarse\n
    en el transcurso de la ejecución del programa. 
    """
    def __init__(self, mensaje="Ingrese una clave existente") -> None:
        """
        Método constructor de la excepción. Se hereda de la clase Exception.
        """
        self.mensaje = mensaje

        super().__init__(self.mensaje)

def verifClave(lista: list, clave: int) -> str:
    """
    Maneja la excepción en que el usuario no introduzca la clave \n
    del producto correctamente.
    """
    if clave - 1 < 0 or clave > len(lista)-1:
        raise(ClaveDesconocida())

class cadenaVacia(Exception):
    """
    Clase para la excepción en que se introduzca una cadena vacía.
    """
    def __init__(self, mensaje="No ingrese cadenas vacias") -> None:
        self.mensaje = mensaje

        super().__init__(self.mensaje)

def verifCadena(cadena: str) -> str:
    """
    Excepción que maneja los casos en que el usuario introduce cadenas vacías.
    """
    if len(cadena) ==  0:
        raise(cadenaVacia())