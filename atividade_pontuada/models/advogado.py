from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereço: Endereço,
                  sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, 
                  rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(id=self._verificar_id_advogado(id), nome=self._verificar_nome_advogado(nome), telefone=self._verificar_telefone_advogado(telefone), cpf=self._verificar_cpf_advogado(cpf),
                          rg=self._verificar_rg_advogado(rg), matricula=self._verificar_matricula_advogado(matricula),
                          email=self._verificar_email_advogado(email), dataNascimento=self._verificar_data_nascimento_advogado(dataNascimento), setor=setor, 
                          salario=self._verificar_salario_advogado(salario), estadoCivil=estadoCivil, sexo=sexo, endereço=endereço)
        self.oab = self.__verificar_oab_advogado(oab)



    def _verificar_id_advogado(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativa(id)

        self.id = id
        return self.id
    
    def _verificar_salario_advogado(self, salario):

        self._verificar_salario_tipo_invalido(salario)
        self._verificar_salario_negativo(salario)

        self.salario = salario
        return self.salario
    
    def _verificar_nome_advogado(self, nome):

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
        if not nome.strip():
            raise TypeError("O nome não deve estar vazio.")
        return nome
    
    def _verificar_cpf_advogado(self, cpf):
        if not cpf.strip():
            raise TypeError("O CPF não deve estar vazio.")
        return cpf
    
    def _verificar_rg_advogado(self, rg):
        if not rg.strip():
            raise TypeError("O rg não deve estar vazio.")
        return rg
    
    def _verificar_matricula_advogado(self, matricula):
        if not matricula.strip():
            raise TypeError("A matricula não deve estar vazia.")
        return matricula
    
    def _verificar_telefone_advogado(self, telefone):
        if not telefone.strip():
            raise TypeError("O telefone não deve estar vazio.")
        
        self.telefone = telefone
        return self.telefone
    
    def _verificar_email_advogado(self, email):
        if not email.strip():
            raise TypeError("O e-mail não deve estar vazio.")
        return email
    
    def _verificar_data_nascimento_advogado(self, dataNascimento):
        if not dataNascimento.strip():
            raise TypeError("A data de nascimento não deve estar vazia.")
        return dataNascimento
    
    def _verificar_salario_tipo_invalido(self, salario):
        if not isinstance(salario, float):
            raise TypeError("O salário deve ser um número real.")
        
    def _verificar_salario_negativo(self, salario):
        if salario <= 0:
            raise ValueError("O salário não deve ser negativo.")
    
    def __verificar_oab_advogado(self, oab):
        if not oab.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(oab, str):
            raise TypeError("valor inválido.")
        return oab
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nOAB: {self.oab}")

     
