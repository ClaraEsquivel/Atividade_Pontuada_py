import pytest
from atividade_pontuada.models.funcionario import Funcionario
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.endereço import Endereço

@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario (123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto), 
            Sexo.FEMININO.texto, EstadoCivil.SOLTEIRO.texto, "18/07/2003", "000.000.000-10", "20.000.000-0", "91164", Setor.SAUDE.texto, 1400.0)
    return funcionario
    
def test_atributo_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "000.000.000-10"

def test_atributo_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "20.000.000-0"

def test_atributo_matricula_valido(funcionario_valido):
    assert funcionario_valido.matricula == "91164"

def test_atributo_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 1400.0

#Teste salário negativo
def test_funcionario_salario__negativo_mensagem_erro(funcionario_valido):
    with pytest.raises(ValueError, match= "O salário não pode ser negativo, informe um salário positivo"):
        Funcionario(123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto), 
            Sexo.FEMININO.texto, EstadoCivil.SOLTEIRO.texto, "18/07/2003", "000.000.000-10", "20.000.000-0", "91164", Setor.SAUDE.texto, -1400.0)

#Teste espaço vazio      
def test_funcionario_cpf_vazio_mensagem_erro(funcionario_valido):
    with pytest.raises(ValueError, match= "O cpf não pode ser vazio, você precisa informar o cpf!"):
        Funcionario(123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto), 
            Sexo.FEMININO.texto, EstadoCivil.SOLTEIRO.texto, "18/07/2003", "", "20.000.000-0", "91164", Setor.SAUDE.texto, 1400.0)
        
def test_funcionario_rg_vazio_mensagem_erro(funcionario_valido):
    with pytest.raises(ValueError, match= "O rg não pode ser vazio, você precisa informar o rg!"):
        Funcionario(123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto), 
            Sexo.FEMININO.texto, EstadoCivil.SOLTEIRO.texto, "18/07/2003", "000.000.000-10", "", "91164", Setor.SAUDE.texto, 1400.0)
        
def test_funcionario_matricula_vazia_mensagem_erro(funcionario_valido):
    with pytest.raises(ValueError, match= "A matrícula não pode ser vazio, você precisa informar a matrícula!"):
        Funcionario(123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto), 
            Sexo.FEMININO.texto, EstadoCivil.SOLTEIRO.texto, "18/07/2003", "000.000.000-10", "20.000.000-0", "", Setor.SAUDE.texto, 1400.0)

