import pytest

from atividade_pontuada.models.advogado import Advogado
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

@pytest.fixture
def advogado_valido():
    advogado = Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", UnidadeFederativa.BAHIA), "BA 123456")
    return advogado

def test_advogado_id_valido(advogado_valido):
    assert advogado_valido.id == 211

def test_advogado_nome_valido(advogado_valido):
    assert advogado_valido.nome == "João"

def test_advogado_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "456.123.785.21"

def test_advogado_rg_valido(advogado_valido):
    assert advogado_valido.rg == "147.258-12"

def test_advogado_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "031.145245"

def test_advogado_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "(71)90000-1111"

def test_advogado_email_valido(advogado_valido):
    assert advogado_valido.email == "adivajoao@gmail.com"

def test_advogado_data_de_nascimento_valido(advogado_valido):
    assert advogado_valido.dataNascimento == "12/07/1982"

def test_advogado_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO

def test_advogado_salario_valido(advogado_valido):
    assert advogado_valido.salario == 7200.0

def test_advogado_EstadoCivil_valido(advogado_valido):
    assert advogado_valido.EstadoCivil == EstadoCivil.CASADO

def test_advogado_sexo_valido(advogado_valido):
    assert advogado_valido.sexo == Sexo.MASCULINO

def test_endereco_advogado_logradouro_valido(advogado_valido):
    assert advogado_valido.endereco.logradouro == "Rua S. José"

def test_endereco_advogado_numero_valido(advogado_valido):
    assert advogado_valido.endereco.numero == "54"

def test_endereco_advogado_complemento_valido(advogado_valido):
    assert advogado_valido.endereco.complemento == "N/D"

def test_endereco_advogado_cep_valido(advogado_valido):
    assert advogado_valido.endereco.cep == "400.156.236"

def test_endereco_advogado_cidade_valido(advogado_valido):
    assert advogado_valido.endereco.cidade == "Salvador"

def test_endereco_advogado_uf_valido(advogado_valido):
    assert advogado_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_advogadoa_OAB_valida(advogado_valido):
    assert advogado_valido.oab == "BA 123456"

def test_advogado_oab_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "")

def test_advogado_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Advogado(-211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")

def test_advogado_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Advogado("211", "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Advogado(211, "", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")   

def test_advogado_cpf_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Advogado(211, "João", "", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Advogado(211, "João", "456.123.785.21", "", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "",
                         "12/07/1982", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        
def test_advogado_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "", Setor.JURIDICO, 7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
        

def test_advogado_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, "7200.0", EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")

def test_advogado_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, -7200.0, EstadoCivil.CASADO, Sexo.MASCULINO, 
                         Endereço("Rua S. José", "54", "N/D", "400.156.236", "Salvador", 
                         UnidadeFederativa.BAHIA), "BA 123456")
