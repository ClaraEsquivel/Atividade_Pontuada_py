from atividade_pontuada.models.pessoa_juridica import Pessoa_Juridica

class Fornecedor:
    def __init__(self, produto:str) -> None:
        self.produto = produto

    def __str__(self) -> str:
        return (
            f"\n Produto: {self.produto}"
        )    