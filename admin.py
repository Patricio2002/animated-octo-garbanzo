class Administrador():
    """
    Esta clase crea un objeto de tipo Administrador. Sus atributos son: 
    Nombre y Contraseña.
    """ 
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.__nombre = nombre
        self.__contraseña = contraseña
        """
        Constructor del objeto tipo Administrados.
        """

    def validacion(self) -> bool:
        """
        Este método valida si el usuario y contraseña introducidos coiniciden con \n
        los presentes en el archivo "administradores.csv".
        """
        with open("administradores.csv", "r") as f:
            for linea in f.readlines():
                linea  = linea.split(sep=',')
                if self.__nombre == linea[0] and (self.__contraseña+'\n' == linea[1] or self.__contraseña == linea[1]):
                    return 1
            return 0
      
    def nuevoAdmin(self) -> None:
        """
        Este método registra a un administrador nuevo en el archivo "administradores.csv"\n
        si se es necesario.
        """
        with open("administradores.csv", "a+") as f:
            f.write(f"\n{self.__nombre},{self.__contraseña}")
                    
            
