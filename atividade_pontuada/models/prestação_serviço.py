from atividade_pontuada.models.pessoa_juridica import Pessoa_Juridica

class Prestacao_Servico:
    def __init__(self, contratoInicio:str, contratoFim:str) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (
            f"\nContrato Início: {self.contratoInicio}"
            f"\ncontrato Fim: {self.contratoFim}"
        )    