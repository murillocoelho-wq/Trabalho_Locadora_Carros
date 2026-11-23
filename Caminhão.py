

from locadora import Veiculo


class Caminhao(Veiculo):
    """Classe que representa um caminhão da locadora."""

    ADICIONAL_POR_TONELADA = 10.0

    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_kg):
        """Inicializa um caminhão.

        Args:
            placa (str): placa do veículo.
            modelo (str): modelo do veículo.
            ano (int): ano de fabricação.
            valor_diaria (float): valor da diária.
            capacidade_kg (float): capacidade de carga em quilos.
        """
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_kg = capacidade_kg

    @property
    def capacidade_kg(self):
        """Retorna a capacidade de carga em quilos."""
        return self.__capacidade_kg

    @capacidade_kg.setter
    def capacidade_kg(self, valor):
        """Define a capacidade de carga, que deve ser maior que zero."""
        if valor <= 0:
            raise ValueError("A capacidade de carga deve ser maior que zero.")
        self.__capacidade_kg = valor

    def capacidade_em_toneladas(self):
        """Retorna a capacidade de carga convertida para toneladas."""
        return self.__capacidade_kg / 1000

    def calcular_aluguel(self, dias):
        """Calcula o aluguel com adicional diário por tonelada.

        Args:
            dias (int): quantidade de dias de aluguel.

        Returns:
            float: valor total do aluguel.
        """
        adicional_diario = self.capacidade_em_toneladas() * self.ADICIONAL_POR_TONELADA
        return (self.valor_diaria + adicional_diario) * dias

    def __str__(self):
        """Exibe os dados do caminhão de forma legível."""
        return (f"[Caminhão] {super().__str__()} | "
                f"Capacidade: {self.__capacidade_kg:.0f} kg")