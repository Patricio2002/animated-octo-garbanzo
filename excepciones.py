class ClaveDesconocida(Exception):
    def __init__(self, mensaje="Ingrese una clave existente") -> None:
        self.mensaje = mensaje

        super().__init__(self.mensaje)

def verifClave(lista, clave):
    if clave - 1 < 0 or clave > len(lista)-1:
        raise(ClaveDesconocida())
