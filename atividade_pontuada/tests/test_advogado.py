import pytest

from atividade_pontuada.models.advogado import Advogado
from atividade_pontuada.models.endereço import Endereço
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa
from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.Sexo import Sexo

@pytest.fixture
def advogado_valido():
    advogado = Advogado(900, "Elton", "(75)98888-0000", "elton.advogado@gmail.com", Sexo.MASCULINO.texto, 
                        EstadoCivil.CASADO.texto, "15/12/1980", "070.777.777-07", "20.555.555", "999", 
                        Setor.JURIDICO.texto, 5000.0, "123456",
                        Endereço("Artêmia", "114E", "Condomínio", "30000-000", "Feira de Santana", UnidadeFederativa.BAHIA.texto) )   
    return advogado

def test_advogafo_id_valido(advogado_valido):
    assert advogado_valido.id == 900

# def test_advogado_salario_valido(advogado_valido):
#     assert advogado_valido.salario == 5000.0

def test_advogado_id_tipo_invalido_mensagem_erro():
    with pytest.raises(ValueError, match="O ID é um número inteiro!"):
        Advogado ("900", "Elton", "(75)98888-0000", "elton.advogado@gmail.com", Sexo.MASCULINO.texto, 
                    EstadoCivil.CASADO.texto, "15/12/1980", "070.777.777-07", "20.555.555", "999", 
                    Setor.JURIDICO.texto, 5000.0, "123456",
                    Endereço("Artêmia", "114E", "Condomínio", "30000-000", "Feira de Santana", UnidadeFederativa.BAHIA.texto))
        
def test_advogado_id_negativo_mensagem_erro():
    with pytest.raises(ValueError, match="O ID não pode ser negativo"):
        Advogado (-900, "Elton", "(75)98888-0000", "elton.advogado@gmail.com", Sexo.MASCULINO.texto, 
                    EstadoCivil.CASADO.texto, "15/12/1980", "070.777.777-07", "20.555.555", "999", 
                    Setor.JURIDICO.texto, 5000.0, "123456",
                    Endereço("Artêmia", "114E", "Condomínio", "30000-000", "Feira de Santana", UnidadeFederativa.BAHIA.texto))
        
# def test_advogado_salario_invalido_mensagem_erro():
#     with pytest.raises(ValueError, match="O salário é um número real!"):
#         Advogado (900, "Elton", "(75)98888-0000", "elton.advogado@gmail.com", Sexo.MASCULINO.texto, 
#                     EstadoCivil.CASADO.texto, "15/12/1980", "070.777.777-07", "20.555.555", "999", 
#                     Setor.JURIDICO.texto, "5000.0", "123456",
#                     Endereço("Artêmia", "114E", "Condomínio", "30000-000", "Feira de Santana", UnidadeFederativa.BAHIA.texto))

# def test_advogado_salario_negativo_mensagem_erro():
#     with pytest.raises(ValueError, match="O salário não pode ser negativo"):
#         Advogado (900, "Elton", "(75)98888-0000", "elton.advogado@gmail.com", Sexo.MASCULINO.texto, 
#                     EstadoCivil.CASADO.texto, "15/12/1980", "070.777.777-07", "20.555.555", "999", 
#                     Setor.JURIDICO.texto, -5000.0, "123456",
#                     Endereço("Artêmia", "114E", "Condomínio", "30000-000", "Feira de Santana", UnidadeFederativa.BAHIA.texto))