import pytest

from atividade_pontuada.models.medico import Medico
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def medico_valido():
    medico = Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
    return medico

def test_medico_id_valido(medico_valido):
    assert medico_valido.id == 455

def test_medico_nome_valido(medico_valido):
    assert medico_valido.nome == "Carla"

def test_medico_cpf_valido(medico_valido):
    assert medico_valido.cpf == "888.777.666.55"

def test_medico_rg_valido(medico_valido):
    assert medico_valido.rg == "111.222-33"

def test_medico_matricula_valido(medico_valido):
    assert medico_valido.matricula == "010.123456"

def test_medico_telefone_valido(medico_valido):
    assert medico_valido.telefone == "(71)90000-1111"

def test_medico_email_valido(medico_valido):
    assert medico_valido.email == "medicarla@gmail.com"

def test_medico_data_de_nascimento_valido(medico_valido):
    assert medico_valido.dataNascimento == "14/03/1965"

def test_medico_setor_valido(medico_valido):
    assert medico_valido.setor == Setor.SAUDE.texto

def test_medico_salario_valido(medico_valido):
    assert medico_valido.salario == 6000

def test_medico_estado_civil_valido(medico_valido):
    assert medico_valido.estadocivil == EstadoCivil.DIVORCIADO.texto

def test_medico_sexo_valido(medico_valido):
    assert medico_valido.sexo == Sexo.FEMININO.texto

def test_endereco_medico_logradouro_valido(medico_valido):
    assert medico_valido.endereço.logradouro == "Rua Vasco da Gama"

def test_endereco_medico_numero_valido(medico_valido):
    assert medico_valido.endereço.numero == "478"

def test_endereco_medico_complemento_valido(medico_valido):
    assert medico_valido.endereço.complemento == "N/D"

def test_endereco_medico_cep_valido(medico_valido):
    assert medico_valido.endereço.cep == "123.456.789"

def test_endereco_medico_cidade_valido(medico_valido):
    assert medico_valido.endereço.cidade == "Rio de Janeiro"

def test_endereco_medico_uf_valido(medico_valido):
    assert medico_valido.endereço.uf == UnidadeFederativa.RIO_DE_JANEIRO.texto

def test_medico_crm_valida(medico_valido):
    assert medico_valido.crm == "147852"

def test_medico_crm_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O CRM não deve ser vazio."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="")
        
def test_medico_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Medico(-455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE.texto, 6000.0, EstadoCivil.DIVORCIADO.texto, Sexo.FEMININO.texto, 
                    Endereço("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.texto), "147852")

def test_medico_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Medico("455", "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE.texto, 6000.0, EstadoCivil.DIVORCIADO.texto, Sexo.FEMININO.texto, 
                    Endereço("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.texto), "147852")
        
def test_medico_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Medico(455, "", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE.texto, 6000.0, EstadoCivil.DIVORCIADO.texto, Sexo.FEMININO.texto, 
                    Endereço("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO.texto), "147852") 

def test_medico_cpf_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Medico(id=455, nome="Carla", cpf="", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="", setor=Setor.SAUDE.texto, salario=6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")
        
def test_medico_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario="6000.0", estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")

def test_medico_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Medico(id=455, nome="Carla", cpf="888.777.666.55", rg="111.222-33", matricula="010.123456", telefone="(71)90000-1111", email="medicarla@gmail.com",
                    dataNascimento="14/03/1965", setor=Setor.SAUDE.texto, salario=-6000.0, estadoCivil=EstadoCivil.DIVORCIADO.texto, sexo=Sexo.FEMININO.texto, 
                    endereço=Endereço(logradouro="Rua Vasco da Gama", numero="478", complemento="N/D", cep="123.456.789", cidade="Rio de Janeiro", uf=UnidadeFederativa.RIO_DE_JANEIRO.texto), crm="147852")