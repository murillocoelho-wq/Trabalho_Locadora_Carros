"""Módulo da classe Moto, filha de Veiculo."""

from locadora import Veiculo


class Moto(Veiculo):
    """Classe que representa uma moto da locadora."""

    LIMITE_CILINDRADAS = 500
    PERCENTUAL_ADICIONAL = 0.10

    def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        """Inicializa uma moto.

        Args:
            placa (str): placa da moto.
            modelo (str): modelo da moto (não pode ser vazio).
            ano (int): ano de fabricação.
            valor_diaria (float): valor da diária em R$ (maior que zero).
            cilindradas (int): cilindradas do motor (cc).
        """
        super().__init__(placa, modelo, ano, valor_diaria)
        self.__alugada = False
        self.cilindradas = cilindradas

    @property
    def cilindradas(self):
        """Retorna as cilindradas da moto."""
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, valor):
        """Define as cilindradas, que devem ser maiores que zero."""
        if valor <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")
        self.__cilindradas = valor

    @property
    def alugada(self):
        """Retorna True se a moto estiver alugada."""
        return self.__alugada

    @alugada.setter
    def alugada(self, valor):
        """Define se a moto está alugada."""
        self.__alugada = bool(valor)

    def eh_alta_cilindrada(self):
        """Retorna True se a moto tiver mais de 500 cc."""
        return self.__cilindradas > self.LIMITE_CILINDRADAS

    def descrever_uso(self):
        """Descreve o tipo de uso da moto."""
        if self.eh_alta_cilindrada():
            return "Moto de alta cilindrada."
        return "Moto de uso geral."

    def calcular_aluguel(self, dias):
        """Calcula o aluguel, com adicional para motos de alta cilindrada.

        Args:
            dias (int): quantidade de dias de aluguel.

        Returns:
            float: valor total do aluguel.
        """
        total = self.valor_diaria * dias
        if self.eh_alta_cilindrada():
            total += total * self.PERCENTUAL_ADICIONAL
        return total

    def __str__(self):
        """Exibe os dados da moto de forma legível."""
        situacao = "Alugada" if self.__alugada else "Disponível"
        return (f"[Moto] {super().__str__()} | "
                f"Cilindradas: {self.__cilindradas} cc | {situacao}")