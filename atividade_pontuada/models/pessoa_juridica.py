from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.endereço import Endereço

class Pessoa_Juridica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereço: Endereço, cnpj: str, inscricaoEstadual:str) -> None:
        super().__init__(id=id, nome=nome, telefone=telefone, email=email, endereço=endereço)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )