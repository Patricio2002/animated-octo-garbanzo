class Administrador():
    def __init__(self, nombre, contraseña) -> None:
        self.nombre = nombre
        self.__contraseña = contraseña

    def bienvenida(self):
        print(f"Bienvenido {self.nombre}")
    
    def datoInvalido(self):
        print("Usuario o contraseña incorrectos")