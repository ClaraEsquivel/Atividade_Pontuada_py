import pytest
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa (123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))
    return pessoa

def test_atributo_id_valido(pessoa_valida):
    assert pessoa_valida.id == 123
    
def test_atributo_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Clara"

def test_pessoa_id_negativo_retorna_mensagem(pessoa_valida):
    with pytest.raises(ValueError, match= "Valor inválido, o ID não pode ser negativo"):
        Pessoa (-123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))

