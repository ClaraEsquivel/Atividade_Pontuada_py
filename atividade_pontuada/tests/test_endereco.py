import pytest
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereço("Terezinha", "900", "casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto)
    return endereco
     
def test_atributo_logradouro_valido(endereco_valido):
    assert endereco_valido.lagradouro == "Terezinha"

def test_atributo_numero_valido(endereco_valido):
    assert endereco_valido.numero == "900"

def test_atributo_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "casa"

def test_atributo_cep_valido(endereco_valido):
    assert endereco_valido.cep == "40711-000"

def test_atributo_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "Salvador"