"""Módulo que define a classe Caminhao, filha de Veiculo."""

from veiculo import Veiculo


class Caminhao(Veiculo):
    """Representa um caminhão disponível para locação."""

    def __init__(self, marca, modelo, placa, diaria_base, capacidade_carga):
        """Inicializa um caminhão.

        Args:
            marca (str): Scania
            modelo (str): 113.
            placa (str): ABCD5UK
            diaria_base (float): 8000
            capacidade_carga (float): 6 toneladas
        """
        super().__init__(marca, modelo, placa, diaria_base)
        self.__capacidade_carga = None
        self.capacidade_carga = capacidade_carga  # usa o setter com validação

    @property
    def capacidade_carga(self):
        """Retorna a capacidade de carga em toneladas."""
        return self.__capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, valor):
        """Define a capacidade de carga, que deve ser maior que zero."""
        if valor <= 0:
            raise ValueError("A capacidade de carga deve ser maior que zero.")
        self.__capacidade_carga = valor

    def calcular_tarifa(self, dias):
        """Calcula o valor do aluguel (sobrescreve o método da classe base).

        O caminhão cobra um adicional de R$ 50,00 por tonelada de capacidade,
        por dia, além da diária base.
        """
        return (self.diaria_base + 50 * self.capacidade_carga) * dias

    def verificar_carga(self, peso):
        """Método próprio: informa se o caminhão suporta o peso informado."""
        return peso <= self.capacidade_carga

    def __str__(self):
        """Retorna os dados do caminhão de forma legível."""
        return f"{super().__str__()} | Caminhão | Capacidade: {self.capacidade_carga} t"