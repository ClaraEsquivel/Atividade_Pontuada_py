from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

class Engenheiro(Funcionario):
    def __init__(self, id:int, nome: str, telefone:str, email:str, endereço:Endereço,
                sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str,
                cpf:str, rg:str, matricula:str, setor:Setor, salario:float, crea:str) -> None:
        super().__init__(id=self._verificar_id_engenheiro(id), nome=self._verificar_nome_engenheiro(nome), cpf=self._verificar_cpf_engenheiro(cpf),
                          rg=self._verificar_rg_engenheiro(rg), matricula=self._verificar_matricula_engenheiro(matricula), telefone=self._verificar_telefone_engenheiro(telefone),
                          email=self._verificar_email_engenheiro(email), dataNascimento=self._verificar_data_nascimento_engenheiro(dataNascimento), setor=setor, 
                          salario=self._verificar_salario_engenheiro(salario),
                            estadoCivil=estadoCivil, sexo=sexo, endereço=endereço)

        self.crea = self.__verificar_crea_engenheiro(crea)

    def _verificar_id_engenheiro(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativa(id)

        self.id = id
        return self.id
    
    def _verificar_salario_engenheiro(self, salario):

        self._verificar_salario_tipo_invalido(salario)
        self._verificar_salario_negativo(salario)

        self.salario = salario
        return self.salario
    
    def _verificar_nome_engenheiro(self, nome):

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
    
    def _verificar_cpf_engenheiro(self, cpf):
        if cpf == "":
            raise TypeError("O CPF não deve estar vazio.")
        return cpf
    
    def _verificar_rg_engenheiro(self, rg):
        if rg == "":
            raise TypeError("O rg não deve estar vazio.")
        return rg
    
    def _verificar_matricula_engenheiro(self, matricula):
        if matricula == "":
            raise TypeError("A matricula não deve estar vazia.")
        return matricula
    
    def _verificar_telefone_engenheiro(self, telefone):
        if telefone == "":
            raise TypeError("O telefone não deve estar vazio.")
        return telefone
    
    def _verificar_email_engenheiro(self, email):
        if email == "":
            raise TypeError("O e-mail não deve estar vazio.")
        return email
    
    def _verificar_data_nascimento_engenheiro(self, dataNascimento):
        if dataNascimento == "":
            raise TypeError("A data de nascimento não deve estar vazia.")
        return dataNascimento
    
    def __verificar_crea_engenheiro(self, crea):
        if not isinstance(crea, str):
            raise TypeError("valor inválido.")
        
        if crea.strip():
            raise ValueError("O CREA não deve ser vazio.")
        
        return crea
    
    def _verificar_salario_tipo_invalido(self, salario):
        if not isinstance(salario, float):
            raise TypeError("O salário deve ser um número real.")
        
    def _verificar_salario_negativo(self, salario):
        if salario <= 0:
            raise ValueError("O salário não deve ser negativo.")


    def __str__(self) -> str:
        return(
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
        )    
        