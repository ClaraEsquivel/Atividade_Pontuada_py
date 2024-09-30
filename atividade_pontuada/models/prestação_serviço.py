from atividade_pontuada.models.pessoa_juridica import Pessoa_Juridica
from atividade_pontuada.models.endereço import Endereço

class Prestacao_Servico(Pessoa_Juridica):
    def __init__(self, id: int, nome:str, telefone:str, email:str, endereco:Endereço,
                 cnpj: str, inscricaoEstadual: str,contratoInicio:str, contratoFim:str) -> None:
       super().__init__(self._verificar_id(id), self._verificar_nome(nome), self._verificar_telefone(telefone), self._verificar_email(email), 
                          endereco, self._verificar_cnpj(cnpj), self._verificar_inscricao_estadual(inscricaoEstadual)),
       self.contratoInicio = self.__verificar_contrato_inicio(contratoInicio)
       self.contratoFim = self.__verificar_contrato_fim(contratoFim)

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
        if nome == "":
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
        if cnpj == "":
            raise TypeError("O CNPJ não deve estar vazio.")
        return cnpj
    
    def _verificar_inscricao_estadual(self, inscricao_estadual):
        if inscricao_estadual == "":
            raise TypeError("A inscrição estadual não deve estar vazia.")
        return inscricao_estadual

    def __verificar_contrato_inicio(self, contratoInicio):
        if contratoInicio == "":
            raise ValueError("Contrato inicio está vazio.")
        if not isinstance(contratoInicio, str):
            raise TypeError("valor inválido.")
        return contratoInicio
    
    def __verificar_contrato_fim(self, contratoFim):
        if contratoFim == "":
            raise ValueError("Contrato fim está vazio.")
        if not isinstance(contratoFim, str):
            raise TypeError("valor inválido.")
        return contratoFim

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nContrato Início: {self.contratoInicio}"
            f"\nContrato Fim: {self.contratoFim}"
        )    