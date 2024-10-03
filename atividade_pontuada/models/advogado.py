from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, 
                 estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, 
                 matricula: str, setor: Setor, salario: float, oab: str, endereco: Endereço) -> None:
        
        super().__init__(self._verificar_id_advogado(id), self._verificar_nome_advogado(nome), 
                         self._verificar_telefone_advogado(telefone), self._verificar_email_advogado(email), 
                         self._verificar_sexo_advogado(sexo), self._verificar_estado_civil_advogado(estadoCivil), 
                         self._verificar_data_nascimenro_advogado(dataNascimento),self._verificar_cpf_advogado(cpf), 
                         self._verificar_rg_advogado(rg), self._verificar_matricula_advogado(matricula), 
                         self._verificar_setor_advogado(setor), self._verificar_salario_advogado(salario),
                         self._verficar_oab_advogado(oab), self._verificar_endereco_advogado(endereco))

#Verificar ID
    def _verificar_id_advogado(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativo(id)

        self.id = id
        return self.id

#Verificar salário   
    # def _verificar_salario_advogado(self, salario):

    #     self._verificar_salario_tipo_invalido(salario)
    #     self._verificar_salario_negativo(salario)

    #     self.salario = salario
    #     return self.salario

#def de ID
    def _verificar_id_tipo_invalido(self, id):
        if not isinstance(id, int):
            raise ValueError("O ID é um número inteiro!")
        return id

    def _verificar_id_negativo(self,id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo")
        if not isinstance(id, int):
           raise TypeError("Valor inválido")
        return id

#def de salario
    # def _verificar_salario_tipo_invalido(self, salario):
    #     if not isinstance(salario, float):
    #         raise ValueError("O salário é um número real!")
    #     return salario

    # def _verificar_salario_negativo(self, salario):
    #     if salario < 0:
    #         raise ValueError("O salário não pode ser negativo")
    #     if not isinstance(salario, float):
    #        raise TypeError("Valor inválido")
    #     return salario




    def __str__(self) -> str:
        return(
            f"{super().__str__()}"
            f"\nOAB: {self.oab}"
        )    