from atividade_pontuada.models.pessoa_juridica import Pessoa_Juridica
from atividade_pontuada.models.endereço import Endereço

class Prestacao_Servico(Pessoa_Juridica):
    def __init__(self, id: int, nome:str, telefone:str, email:str, endereco:Endereço,
                 cnpj: str, inscricaoEstadual: str,contratoInicio:str, contratoFim:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nContrato Início: {self.contratoInicio}"
            f"\nContrato Fim: {self.contratoFim}"
        )    