
"""Módulo da classe Carro, filha de Veiculo."""

from locadora import Veiculo


class Carro(Veiculo):
    """Classe que representa um carro da locadora."""

    DIAS_PARA_DESCONTO = 7
    PERCENTUAL_DESCONTO = 0.10

    def __init__(self, placa, modelo, ano, valor_diaria, numero_portas):
        """Inicializa um carro.

        Args:
            placa (str): placa do veículo.
            modelo (str): modelo do veículo.
            ano (int): ano de fabricação.
            valor_diaria (float): valor da diária.
            numero_portas (int): quantidade de portas do carro.
        """
        super().__init__(placa, modelo, ano, valor_diaria)
        self.numero_portas = numero_portas

    @property
    def numero_portas(self):
        """Retorna o número de portas do carro."""
        return self.__numero_portas

    @numero_portas.setter
    def numero_portas(self, valor):
        """Define o número de portas, que deve estar entre 2 e 5."""
        if valor < 2 or valor > 5:
            raise ValueError("O número de portas deve estar entre 2 e 5.")
        self.__numero_portas = valor

    def eh_familiar(self):
        """Retorna True se o carro tiver 4 portas ou mais."""
        return self.__numero_portas >= 4

    def calcular_aluguel(self, dias):
        """Calcula o aluguel, com desconto para aluguéis longos.

        Args:
            dias (int): quantidade de dias de aluguel.

        Returns:
            float: valor total do aluguel.
        """
        total = self.valor_diaria * dias
        if dias >= self.DIAS_PARA_DESCONTO:
            total -= total * self.PERCENTUAL_DESCONTO
        return total

    def __str__(self):
        """Exibe os dados do carro de forma legível."""
        return f"[Carro] {super().__str__()} | Portas: {self.__numero_portas}"