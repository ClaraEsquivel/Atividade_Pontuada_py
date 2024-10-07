import pytest

from atividade_pontuada.models.cliente import Cliente
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    cliente = Cliente(555, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)
    return cliente

def test_cliente_id_valido(cliente_valido):
    assert cliente_valido.id == 555

def test_cliente_nome_valido(cliente_valido):
    assert cliente_valido.nome == "Almiro"

def test_cliente_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "(71)98888-6666"

def test_cliente_email_valido(cliente_valido):
     assert cliente_valido.email == "almiro@gmail.com"

# def test_endereco_cliente_logradouro_valido(cliente_valido):
#     assert cliente_valido.endereço.logradouro == "Rio Sena"

# def test_endereco_cliente_numero_valido(cliente_valido):
#     assert cliente_valido.endereço.numero == "900"

# def test_endereco_cliente_complemento_valido(cliente_valido):
#     assert cliente_valido.endereço.complemento == "Casa"

# def test_endereco_cliente_cep_valido(cliente_valido):
#     assert cliente_valido.endereço.cep == "40600-006"

# def test_endereco_cliente_cidade_valido(cliente_valido):
#     assert cliente_valido.endereço.cidade == "Salvador"

# def test_endereco_cliente_uf_valido(cliente_valido):
#     assert cliente_valido.endereço.uf == UnidadeFederativa.BAHIA.texto

def test_cliente_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloAtemdimento == 144

def test_cliente_sexo_valido(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO.texto

def test_cliente_estado_civil_valido(cliente_valido):
    assert cliente_valido.estadocivil == EstadoCivil.SEPARADO
    
def test_cliente_data_de_nascimento_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "12/05/1980"

def test_cliente_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        cliente = Cliente(-555, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)

def test_cliente_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        cliente = Cliente(555.6, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)
        
def test_cliente_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     cliente = Cliente(555, "", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)

def test_cliente_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        cliente = Cliente(555, "Almiro", "", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)

def test_cliente_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        cliente = Cliente(555, "Almiro", "(71)98888-6666", "", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144)

def test_cliente_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        cliente = Cliente(555, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"", 144)
        
def test_cliente_protocolo_atendimento_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser um número inteiro."):
        cliente = Cliente(555, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", 144.6)

def test_cliente_protocolo_atendimento_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O protocolo de atendimento não pode ser negativo."):
        cliente = Cliente(555, "Almiro", "(71)98888-6666", "almiro@gmail.com", 
                      Endereço("Rio sena", "900", "Casa", "40600-006", "Salvador", UnidadeFederativa.BAHIA.texto), 
                      Sexo.MASCULINO.texto, EstadoCivil.SEPARADO,"12/05/1980", -144)
   