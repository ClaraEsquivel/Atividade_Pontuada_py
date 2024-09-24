from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

class Medico(Funcionario):
    def __init__(self, nome: str, telefone:str, email:str, endereco:Endereço,
                sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str,
                cpf:str, rg:str, matricula:str, setor:Setor, salario:float, crm:str) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crm = crm

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCRM: {self.crm}"
        )    