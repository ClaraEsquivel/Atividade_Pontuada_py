from enum import Enum

class Sexo (Enum):
    FEMININO = ("Feminino", "F")
    MASCULINO = ("Masculino", "M")

    def __init__(self, texto:str, caracter:str) -> None:
        self.texto = texto
        self.caracter = caracter