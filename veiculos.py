"""Módulo da classe base Veiculo."""


class Veiculo:
    """Classe base que representa um veículo da locadora."""

    def __init__(self, placa, modelo, ano, valor_diaria):
        """Inicializa um veículo.

        Args:
            placa (str): placa do veículo.
            modelo (str): modelo do veículo.
            ano (int): ano de fabricação.
            valor_diaria (float): valor da diária de aluguel.
        """
        self.__placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    @property
    def placa(self):
        """Retorna a placa do veículo."""
        return self.__placa

    @property
    def modelo(self):
        """Retorna o modelo do veículo."""
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        """Define o modelo, não permitindo valor vazio."""
        if not valor or not valor.strip():
            raise ValueError("O modelo não pode ser vazio.")
        self.__modelo = valor.strip()

    @property
    def ano(self):
        """Retorna o ano de fabricação."""
        return self.__ano

    @ano.setter
    def ano(self, valor):
        """Define o ano, não permitindo valores menores que 1900."""
        if valor < 1900:
            raise ValueError("Ano inválido.")
        self.__ano = valor

    @property
    def valor_diaria(self):
        """Retorna o valor da diária."""
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor):
        """Define a diária, que deve ser maior que zero."""
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias):
        """Calcula o valor do aluguel (comportamento base).

        Args:
            dias (int): quantidade de dias de aluguel.

        Returns:
            float: valor total do aluguel.
        """
        return self.__valor_diaria * dias

    def __str__(self):
        """Exibe os dados do veículo de forma legível."""
        return (f"Placa: {self.__placa} | Modelo: {self.__modelo} | "
                f"Ano: {self.__ano} | Diária: R$ {self.__valor_diaria:.2f}")