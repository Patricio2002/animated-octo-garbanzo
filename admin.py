class Administrador():
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.__nombre = nombre
        self.__contraseña = contraseña

    def validacion(self):
        with open("administradores.csv", "r") as f:
            for linea in f.readlines():
                linea  = linea.split(sep=',')
                if self.__nombre == linea[0] and (self.__contraseña+'\n' == linea[1] or self.__contraseña == linea[1]):
                    return 1
            return 0
    def nuevoAdmin(self):
        with open("administradores.csv", "a+") as f:
            f.write(f"\n{self.__nombre},{self.__contraseña}")
                    
            
