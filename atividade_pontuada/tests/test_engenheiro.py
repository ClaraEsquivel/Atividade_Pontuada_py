import pytest

from atividade_pontuada.models.engenheiro import Engenheiro
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(id=566, nome="Amanda", cpf="999.123.781.21", rg="147.666-12", matricula="031.123456", telefone="(71)90000-1111", email="engamanda@gmail.com",
                         dataNascimento="03/10/2000", setor=Setor.ENGENHARIA.texto, salario=5400.0, estadoCivil=EstadoCivil.SOLTEIRO.texto, sexo=Sexo.FEMININO.texto, 
                         endereço=Endereço(logradouro="Rua Flores", numero="15", complemento="N/D", cep="400.356.236", cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO.texto), crea="4523698")
    return engenheiro

def test_engenheiro_id_valido(engenheiro_valido):
    assert engenheiro_valido.id == 566

def test_engenheiro_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Amanda"

def test_engenheiro_cpf_valido(engenheiro_valido):
    assert engenheiro_valido.cpf == "999.123.781.21"

def test_engenheiro_rg_valido(engenheiro_valido):
    assert engenheiro_valido.rg == "147.666-12"

def test_engenheiro_matricula_valido(engenheiro_valido):
    assert engenheiro_valido.matricula == "031.123456"

def test_engenheiro_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "(71)90000-1111"

def test_advogado_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "engamanda@gmail.com"

def test_engenheiro_data_de_nascimento_valido(engenheiro_valido):
    assert engenheiro_valido.dataNascimento == "03/10/2000"

def test_engenheiro_setor_valido(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA.texto

def test_engenheiro_salario_valido(engenheiro_valido):
    assert engenheiro_valido.salario == 5400.0

def test_engenheiro_estado_civil_valido(engenheiro_valido):
    assert engenheiro_valido.estadocivil == EstadoCivil.SOLTEIRO.texto

def test_engenheiro_sexo_valido(engenheiro_valido):
    assert engenheiro_valido.sexo == Sexo.FEMININO.texto

def test_endereco_engenheiro_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.logradouro == "Rua Flores"

def test_endereco_engenheiro_numero_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.numero == "15"

def test_endereco_engenheiro_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.complemento == "N/D"

def test_endereco_engenheiro_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.cep == "400.356.236"

def test_endereco_engenheiro_cidade_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.cidade == "São Paulo"

def test_endereco_engenheiro_uf_valido(engenheiro_valido):
    assert engenheiro_valido.endereço.uf == UnidadeFederativa.SAO_PAULO.texto

def test_engenheiro_crea_valida(engenheiro_valido):
    assert engenheiro_valido.crea == "4523698"

def test_engenheiro_crea_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O CREA não deve ser vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "")
        
def test_engenheiro_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Engenheiro(-566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")

def test_engenheiro_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Engenheiro("566", "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        
def test_engenheiro_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Engenheiro(566, "", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")  

def test_engenheiro_cpf_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Engenheiro(566, "Amanda", "", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        
def test_engenheiro_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        
def test_engenheiro_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        
def test_engenheiro_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        
def test_engenheiro_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
         Engenheiro(id=566, nome="Amanda", cpf="999.123.781.21", rg="147.666-12", matricula="031.123456", telefone="(71)90000-1111", email="engamanda@gmail.com",
                         dataNascimento="03/10/2000", setor=Setor.ENGENHARIA, salario=5400.0, estadoCivil=EstadoCivil.SOLTEIRO, sexo=Sexo.FEMININO, 
                         endereço=Endereço(logradouro="Rua Flores", numero="15", complemento="N/D", cep="400.356.236", cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO), crea="4523698")

        
def test_engenheiro_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "", Setor.ENGENHARIA, 5400.0, EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")
        

def test_engenheiro_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, "5400.0", EstadoCivil.SOLTEIRO, Sexo.FEMININO, 
                         Endereço("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", UnidadeFederativa.SAO_PAULO), "4523698")

def test_engenheiro_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Engenheiro(id=566, nome="Amanda", cpf="999.123.781.21", rg="147.666-12", matricula="031.123456", telefone="(71)90000-1111", email="engamanda@gmail.com",
                         dataNascimento="03/10/2000", setor=Setor.ENGENHARIA, salario=-5400.0, estadoCivil=EstadoCivil.SOLTEIRO, sexo=Sexo.FEMININO, 
                         endereço=Endereço(logradouro="Rua Flores", numero="15", complemento="N/D", cep="400.356.236", cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO), crea="4523698")
