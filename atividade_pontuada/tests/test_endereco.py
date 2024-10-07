import pytest
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereço("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto)
    return endereco
     
def test_atributo_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Terezinha"

def test_atributo_numero_valido(endereco_valido):
    assert endereco_valido.numero == "900"

def test_atributo_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Casa"

def test_atributo_cep_valido(endereco_valido):
    assert endereco_valido.cep == "40711-000"

def test_atributo_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

#Teste mensagem vazia
def test_logradouro_endereco_vazio_mensagem_erro(endereco_valido):
    with pytest.raises(ValueError, match= "O logradouro não pode ser vazio, você precisa informar o logradouro!"):
        Endereço ("", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto)  

def test_numero_endereco_vazio_mensagem_erro(endereco_valido):
    with pytest.raises(ValueError, match= "O número não pode ser vazio, você precisa informar o número!"):
        Endereço ("Terezinha", "", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto) 

def test_complemento_endereco_vazio_mensagem_erro(endereco_valido):
    with pytest.raises(ValueError, match= "O complemento não pode ser vazio, você precisa informar o complemento!"):
        Endereço ("Terezinha", "900", "", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto)  

def test_cep_endereco_vazio_mensagem_erro(endereco_valido):
    with pytest.raises(ValueError, match= "O cep não pode ser vazio, você precisa informar o cep!"):
        Endereço ("Terezinha", "900", "Casa", "", "Salvador", UnidadeFederativa.BAHIA.texto)  

def test_cidade_endereco_vazio_mensagem_erro(endereco_valido):
    with pytest.raises(ValueError, match= "O nome da cidade não pode ser vazio, você precisa informar o cidade!"):
        Endereço ("Terezinha", "900", "Casa", "40711-000", "", UnidadeFederativa.BAHIA.texto)  