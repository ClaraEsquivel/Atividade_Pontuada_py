from atividade_pontuada.models.pessoa_fisica import Pessoa_Fisica
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Sexo import Sexo

class Cliente(Pessoa_Fisica):
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereco:Endereço,
                 sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str, protocoloAtendimento:int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProtocolo de Atendimento"
        )    