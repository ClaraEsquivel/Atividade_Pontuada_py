from atividade_pontuada.models.pessoa_juridica import Pessoa_Juridica
from atividade_pontuada.models.endereço import Endereço

class Fornecedor(Pessoa_Juridica):
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereço:Endereço, cnpj: str, inscricaoEstadual: str, produto:str) -> None:
        super().__init__(id=self._verificar_id(id), nome=self._verificar_nome(nome), telefone=self._verificar_telefone(telefone), email=self._verificar_email(email), 
                         endereço=endereço, cnpj=self._verificar_cnpj(cnpj), inscricaoEstadual=self._verificar_inscricao_estadual(inscricaoEstadual))
        
        self.produto = self._verificar_produto_fornecedor(produto)

    def _verificar_produto_fornecedor(self, produto):

        self._verificar_produto_vazio_invalido(produto)

        self.produto = produto
        return self.produto

    def _verificar_id(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativa(id)

        self.id = id
        return self.id
    
    def _verificar_nome(self, nome):

        self._verificar_nome_vazio_invalido(nome)

        self.nome = nome
        return self.nome


    def _verificar_id_tipo_invalido(self, id):
        if not isinstance(id, int):
            raise TypeError("O id deve ser um número inteiro.")

    def _verificar_id_negativa(self, id):
        if id <= 0:
            raise ValueError("O id não pode ser negativo.")
        
    def _verificar_nome_vazio_invalido(self, nome):
        if nome.strip():
            raise TypeError("O nome não deve estar vazio.")
        return nome
    
    def _verificar_telefone(self, telefone):
        if telefone == "":
            raise TypeError("O telefone não deve estar vazio.")
        return telefone
    
    def _verificar_email(self, email):
        if email == "":
            raise TypeError("O e-mail não deve estar vazio.")
        return email
    
    def _verificar_cnpj(self, cnpj):
        if cnpj.strip():
            raise ValueError("O CNPJ não deve estar vazio.")
        return cnpj
    
    def _verificar_inscricao_estadual(self, inscricao_estadual):
        if inscricao_estadual.strip():
            raise ValueError("A inscrição estadual não deve estar vazia.")
        return inscricao_estadual

    def _verificar_produto_vazio_invalido(self, produto):
        if produto == "":
            raise TypeError("O produto não deve estar vazio.")
        return produto


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n Produto: {self.produto}"
        )    