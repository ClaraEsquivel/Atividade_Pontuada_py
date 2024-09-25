from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.pessoa_fisica import Pessoa_Fisica
from atividade_pontuada.models.endereço import Endereço


class Funcionario(Pessoa_Fisica):
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereco:Endereço,
                 sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str, cpf:str, rg:str, 
                 matricula:str, setor:Setor, salario:float) -> None:
        
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = self.__verificar_cpf_funcionario(cpf)
        self.rg = self.__verificar_rg_funcionario(rg)
        self.matricula = self.__verificar_matricula_funcionario(matricula)
        self.setor = setor
        self.salario = self.__verificar_salario_funcionario(salario)

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.texto}"
            f"\nSalário: {self.salario}"
            
        )
    

    def __verificar_cpf_funcionario(self, cpf):
        if cpf == "":
            raise ValueError("O cpf não pode ser vazio, você precisa informar o cpf!")
        if not isinstance(cpf, str):
            raise TypeError("Valor inválido")
        return cpf 
    
    # def __verificar_rg_funcionario(self, rg):
    #     if rg == "":
    #         raise ValueError("O rg não pode ser vazio, você precisa informar o rg!")
    #     if not isinstance(rg, str):
    #         raise TypeError("Valor inválido")
    #     return rg
    
    # def __verificar_matricula_funcionario(self, matricula):
    #     if matricula == "":
    #         raise ValueError("A matricula não pode ser vazia, você precisa informar a matrícula!")
    #     if not isinstance(matricula, str):
    #         raise TypeError("Valor inválido")
    #     return matricula
    
    # def __verificar_salario_funcionario(self, salario):
    #     if salario < 0:
    #         raise ValueError("O salário não pode ser negativo, informe um salário positivo")
    #     if not isinstance(salario, float):
    #        raise TypeError("Valor incorreto")
    #     return salario
    