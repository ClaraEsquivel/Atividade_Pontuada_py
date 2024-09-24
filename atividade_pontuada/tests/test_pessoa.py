import pytest
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa (123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))
    return pessoa

def test_atributo_id_valido(pessoa_valida):
    assert pessoa_valida.id == 123
    
def test_atributo_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Clara"

def test_pessoa_alternar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Cerise"
    assert pessoa_valida.nome == "Cerise"

def test_pessoa_id_negativo_mensagem_erro(pessoa_valida):
    with pytest.raises(ValueError, match= "Valor inválido, o ID não pode ser negativo"):
        Pessoa (-123, "Clara", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))

def test_nome_pessoa_vazio_mensagem_erro(pessoa_valida):
    with pytest.raises(ValueError, match= "O nome não pode ser vazio, você precisa informar o nome!"):
        Pessoa (123, "", "(71)99111-2222", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))
        
def test_telefone_pessoa_vazio_mensagem_erro(pessoa_valida):
    with pytest.raises(ValueError, match= "O telefone não pode ser vazio, você precisa informar o telefone!"):
        Pessoa (123, "Clara", "", "clara@gmail.com", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))

def test_email_pessoa_vazio_mensagem_erro(pessoa_valida):
    with pytest.raises(ValueError, match= "O email não pode ser vazio, você precisa informar o email!"):
        Pessoa (123, "Clara", "(71)99111-2222", "", 
            Endereço ("Terezinha", "900", "Casa", "40711-000", "Salvador", UnidadeFederativa.BAHIA.texto))