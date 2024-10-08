import pytest

from atividade_pontuada.models.advogado import Advogado
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

@pytest.fixture
def advogado_valido():
    advogado = Advogado(id=123, nome="Elton", telefone="(75)98888-8888", email="elton@gmail.com", 
                        endereço=Endereço(logradouro="Artêmia", numero="155", complemento="Casa", cep="40700.000", cidade="Feira de Santana", uf=UnidadeFederativa.BAHIA.texto), 
                        sexo=Sexo.MASCULINO.texto, estadoCivil=EstadoCivil.CASADO.texto, dataNascimento="15/12/1985", cpf="089.000.000-88", 
                        rg="20.000.000-20", matricula="1111", setor=Setor.JURIDICO.texto, salario=5000.0, oab="40711")
    return advogado

def test_advogado_id_valido(advogado_valido):
    assert advogado_valido.id == 123

def test_advogado_nome_valido(advogado_valido):
    assert advogado_valido.nome == "Elton"

def test_advogado_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "(75)98888-8888"

def test_advogado_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "089.000.000-88"

def test_advogado_rg_valido(advogado_valido):
    assert advogado_valido.rg == "20.000.000-20"

def test_advogado_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "1111"

def test_advogado_email_valido(advogado_valido):
    assert advogado_valido.email == "elton@gmail.com"

def test_advogado_data_de_nascimento_valido(advogado_valido):
    assert advogado_valido.dataNascimento == "15/12/1985"

def test_advogado_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO.texto

def test_advogado_salario_valido(advogado_valido):
    assert advogado_valido.salario == 5000.0

def test_advogado_estado_civil_valido(advogado_valido):
    assert advogado_valido.estadocivil == EstadoCivil.CASADO.texto

def test_advogado_sexo_valido(advogado_valido):
    assert advogado_valido.sexo == Sexo.MASCULINO.texto

def test_endereço_advogado_logradouro_valido(advogado_valido):
    assert advogado_valido.endereço.logradouro == "Artêmia"

def test_endereço_advogado_numero_valido(advogado_valido):
    assert advogado_valido.endereço.numero == "155"

def test_endereço_advogado_complemento_valido(advogado_valido):
    assert advogado_valido.endereço.complemento == "Casa"

def test_endereço_advogado_cep_valido(advogado_valido):
    assert advogado_valido.endereço.cep == "40700.000"

def test_endereço_advogado_cidade_valido(advogado_valido):
    assert advogado_valido.endereço.cidade == "Feira de Santana"

def test_endereço_advogado_uf_valido(advogado_valido):
    assert advogado_valido.endereço.uf == UnidadeFederativa.BAHIA.texto

def test_advogadoa_OAB_valida(advogado_valido):
    assert advogado_valido.oab == "40711"

#OAB
def test_advogado_oab_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "")

#ID
def test_advogado_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Advogado(-123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")

def test_advogado_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Advogado(123.3, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")
        

#Nome        
def test_advogado_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Advogado(123, "", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")

#CPF    
def test_advogado_cpf_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")
        

#RG        
def test_advogado_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")
       
#Matricula      
def test_advogado_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "" ,Setor.JURIDICO.texto, 
                        5000.0, "40711")

#Telefone      
def test_advogado_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Advogado(123, "Elton", "", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")

#Email              
def test_advogado_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Advogado(123, "Elton", "(75) 98888-8888", "", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")

#Data de nascimento              
def test_advogado_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000.0, "40711")

#Salário             
def test_advogado_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        5000, "40711")
      
def test_advogado_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Advogado(123, "Elton", "(75) 98888-8888", "elton@gmail.com", 
                        Endereço("Artêmia", "155", "Casa", "40700.000", "Feira de Santana", 
                        UnidadeFederativa.BAHIA.texto), Sexo.MASCULINO.texto, EstadoCivil.CASADO.texto, 
                        "15/12/1985", "089.000.000-88", "20.000.000-20", "1111",Setor.JURIDICO.texto, 
                        -5000.0, "40711")
     