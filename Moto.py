"""Módulo com a classe base Moto."""


class Moto:
    """Classe base que representa uma moto disponível para aluguel."""

    def __init__(self, modelo, placa, ano, valor_diaria):
        """Cria uma moto.

        Args:
            modelo (str): modelo da moto (não pode ser vazio).
            placa (str): placa da moto (não pode ser vazia).
            ano (int): ano de fabricação (entre 1980 e 2100).
            valor_diaria (float): valor da diária em R$ (maior que zero).
        """
        self.__modelo = None
        self.__placa = None
        self.__ano = None
        self.__valor_diaria = None
        self.__alugada = False
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.valor_diaria = valor_diaria

    @property
    def modelo(self):
        """Retorna o modelo da moto."""
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        """Define o modelo, recusando valores vazios."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O modelo não pode ser vazio.")
        self.__modelo = valor.strip()

    @property
    def placa(self):
        """Retorna a placa da moto."""
        return self.__placa

    @placa.setter
    def placa(self, valor):
        """Define a placa, recusando valores vazios."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A placa não pode ser vazia.")
        self.__placa = valor.strip().upper()

    @property
    def ano(self):
        """Retorna o ano de fabricação."""
        return self.__ano

    @ano.setter
    def ano(self, valor):
        """Define o ano, recusando anos fora do intervalo 1980-2100."""
        if valor < 1980 or valor > 2100:
            raise ValueError("O ano deve estar entre 1980 e 2100.")
        self.__ano = valor

    @property
    def valor_diaria(self):
        """Retorna o valor da diária em R$."""
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor):
        """Define a diária, recusando zero ou valores negativos."""
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    @property
    def alugada(self):
        """Retorna True se a moto está alugada."""
        return self.__alugada

    @alugada.setter
    def alugada(self, valor):
        """Define se a moto está alugada."""
        self.__alugada = bool(valor)

    def calcular_aluguel(self, dias):
        """Retorna o valor do aluguel para a quantidade de dias.

        Método sobrescrito nas classes filhas.
        """
        return self.__valor_diaria * dias

    def descrever_uso(self):
        """Retorna uma frase sobre o uso ideal da moto (sobrescrito)."""
        return "Moto de uso geral."

    def __str__(self):
        """Retorna os dados da moto de forma legível."""
        situacao = "Alugada" if self.__alugada else "Disponível"
        return (f"{type(self).__name__}: {self.__modelo} | Placa {self.__placa} | "
                f"{self.__ano} | R$ {self.__valor_diaria:.2f}/dia | {situacao}")