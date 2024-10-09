import pytest

from atividade_pontuada.models.fornecedor import Fornecedor
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(id=333, nome="Valeria", telefone="(71)90000-1111", email="dorvaleria@gmail.com", 
                            endereço=Endereço(logradouro="Rua Salgueiro", numero="14", complemento="N/D", cep="178.147.123", 
                            cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO.texto),cnpj="123.654", inscricaoEstadual="15", produto="Café")
    return fornecedor

def test_fornecedor_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 333

def test_fornecedor_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Valeria"

def test_fornecedor_telefone_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "(71)90000-1111"

def test_fornecedor_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "dorvaleria@gmail.com"

def test_fornecedor_cnpj_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "123.654"

def test_fornecedor_inscricao_estadual_valido(fornecedor_valido):
    assert fornecedor_valido.inscricaoEstadual == "15"

def test_cliente_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Café"

def test_endereco_fornecedor_logradouro_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.logradouro == "Rua Salgueiro"

def test_endereco_fornecedor_numero_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.numero == "14"

def test_endereco_fornecedor_complemento_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.complemento == "N/D"

def test_endereco_fornecedor_cep_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.cep == "178.147.123"

def test_endereco_fornecedor_cidade_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.cidade == "São Paulo"

def test_endereco_fornecedor_uf_valido(fornecedor_valido):
    assert fornecedor_valido.endereço.uf == UnidadeFederativa.SAO_PAULO.texto

def test_fornecedor_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Fornecedor(-333, "Valeria", "(71)90000-1111", "dorvaleria@gmail.com", "123.654", "15", "Café",
                            Endereço("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", UnidadeFederativa.SAO_PAULO.texto))

def test_fornecedor_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Fornecedor("333", "Valeria", "(71)90000-1111", "dorvaleria@gmail.com", "123.654", "15", "Café",
                            Endereço("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", UnidadeFederativa.SAO_PAULO.texto))
        
def test_fornecedor_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Fornecedor(333, "", "(71)90000-1111", "dorvaleria@gmail.com", "123.654", "15", "Café",
                            Endereço("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", UnidadeFederativa.SAO_PAULO.texto))

def test_fornecedor_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Fornecedor(333, "Valeria", "", "dorvaleria@gmail.com", "123.654", "15", "Café",
                            Endereço("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", UnidadeFederativa.SAO_PAULO.texto))
        
def test_fornecedor_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Fornecedor(333, "Valeria", "(71)90000-1111", "", "123.654", "15", "Café",
                            Endereço("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", UnidadeFederativa.SAO_PAULO.texto))
        
def test_fornecedor_cnpj_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CNPJ não deve estar vazio."):
        Fornecedor(id=333, nome="Valeria", telefone="(71)90000-1111", email="dorvaleria@gmail.com", 
                            endereço=Endereço(logradouro="Rua Salgueiro", numero="14", complemento="N/D", cep="178.147.123", 
                            cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO.texto),cnpj="", inscricaoEstadual="15", produto="Café")
        
def test_fornecedor_inscricao_estadual_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A inscrição estadual não deve estar vazia."):
        Fornecedor(id=333, nome="Valeria", telefone="(71)90000-1111", email="dorvaleria@gmail.com", 
                            endereço=Endereço(logradouro="Rua Salgueiro", numero="14", complemento="N/D", cep="178.147.123", 
                            cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO.texto),cnpj="123.654", inscricaoEstadual="", produto="Café")

def test_fornecedor_produto_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O produto não deve estar vazio."):
        Fornecedor(id=333, nome="Valeria", telefone="(71)90000-1111", email="dorvaleria@gmail.com", 
                            endereço=Endereço(logradouro="Rua Salgueiro", numero="14", complemento="N/D", cep="178.147.123", 
                            cidade="São Paulo", uf=UnidadeFederativa.SAO_PAULO.texto),cnpj="123.654", inscricaoEstadual="15", produto="")