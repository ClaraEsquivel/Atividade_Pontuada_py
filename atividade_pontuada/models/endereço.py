from atividade_pontuada.models.enums.UnidadeFederativa import UnidadeFederativa

class Endereço:
    def __init__(self, lagradouro:str, numero:str, complemento:str, cep:str, cidade:str, uf:UnidadeFederativa) -> None:
        self.lagradouro = self.__verificar_lagradouro_endereco(lagradouro)
        self.numero = self.__verificar_numero_endereco(numero)
        self.complemento = self.__verificar_complemento_endereco(complemento)
        self.cep = self.__verificar_cep_endereco(cep)
        self.cidade = self. __verificar_cidade_endereco(cidade)
        self.uf = uf


    def __str__(self) -> str:
        return (
            f"\nLagradouro: {self.lagradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUF: {self.uf.texto}"
        )    

    def __verificar_lagradouro_endereco(self, lagradouro):
        if lagradouro == "":
            raise ValueError("O lagradouro não pode ser vazio, você precisa informar o lagradouro!")
        if not isinstance(lagradouro, str):
            raise TypeError("Valor inválido")
        return lagradouro 
    
    def __verificar_numero_endereco(self, numero):
        if numero == "":
            raise ValueError("O número não pode ser vazio, você precisa informar o número!")
        if not isinstance(numero, str):
            raise TypeError("Valor inválido")
        return numero
    
    def __verificar_complemento_endereco(self, complemento):
        if complemento == "":
            raise ValueError("O complemento não pode ser vazio, você precisa informar o complemento!")
        if not isinstance(complemento, str):
            raise TypeError("Valor inválido")
        return complemento
    
    def __verificar_cep_endereco(self, cep):
        if cep == "":
            raise ValueError("O cep não pode ser vazio, você precisa informar o cep!")
        if not isinstance(cep, str):
            raise TypeError("Valor inválido")
        return cep
    
    def __verificar_cidade_endereco(self, cidade):
        if cidade == "":
            raise ValueError("O nome da cidade não pode ser vazio, você precisa informar o cidade!")
        if not isinstance(cidade, str):
            raise TypeError("Valor inválido")
        return cidade
    
   