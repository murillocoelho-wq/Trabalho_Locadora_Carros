"""Módulo com a classe base Veiculo e a classe Locadora."""


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


class Locadora:
    """Classe que gerencia o cadastro e o aluguel de veículos."""

    def __init__(self, nome):
        """Inicializa a locadora.

        Args:
            nome (str): nome da locadora.
        """
        self.__nome = nome
        self.__veiculos = []

    @property
    def nome(self):
        """Retorna o nome da locadora."""
        return self.__nome

    def cadastrar(self, veiculo):
        """Cadastra um veículo, não permitindo placa repetida.

        Args:
            veiculo (Veiculo): veículo a ser cadastrado.
        """
        if self.buscar_por_placa(veiculo.placa) is not None:
            raise ValueError(f"Já existe um veículo com a placa {veiculo.placa}.")
        self.__veiculos.append(veiculo)

    def listar(self):
        """Retorna uma cópia da lista de veículos cadastrados."""
        return list(self.__veiculos)

    def buscar_por_placa(self, placa):
        """Busca um veículo pela placa.

        Args:
            placa (str): placa a ser procurada.

        Returns:
            Veiculo | None: o veículo encontrado ou None.
        """
        placa = str(placa).strip().upper()
        for veiculo in self.__veiculos:
            if veiculo.placa.strip().upper() == placa:
                return veiculo
        return None

    def simular_alugueis(self, dias):
        """Calcula o aluguel de todos os veículos (polimorfismo).

        Args:
            dias (int): quantidade de dias de aluguel.

        Returns:
            list: lista de tuplas (veiculo, valor).
        """
        return [(veiculo, veiculo.calcular_aluguel(dias))
                for veiculo in self.__veiculos]

    def __str__(self):
        """Exibe o nome da locadora e a quantidade de veículos."""
        return f"{self.__nome} - {len(self.__veiculos)} veículo(s) cadastrado(s)"