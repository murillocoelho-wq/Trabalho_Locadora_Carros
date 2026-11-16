"""Programa principal da locadora de veículos (menu no terminal)."""

from caminhao import Caminhao
from carro import Carro
from locadora import Locadora
from moto import Moto


def ler_texto(mensagem):
    """Lê um texto do usuário com input()."""
    return input(mensagem).strip()


def ler_inteiro(mensagem):
    """Lê um número inteiro do usuário, repetindo até ser válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_decimal(mensagem):
    """Lê um número decimal do usuário, repetindo até ser válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 120.50).")


def exibir_menu():
    """Exibe as opções do menu."""
    print("\n===== LOCADORA DE VEÍCULOS =====")
    print("1 - Cadastrar veículo")
    print("2 - Listar veículos")
    print("3 - Buscar veículo por placa")
    print("4 - Calcular aluguel de todos os veículos (polimorfismo)")
    print("0 - Sair")


def cadastrar_veiculo(locadora):
    """Pede os dados ao usuário, cria o veículo e cadastra na locadora."""
    print("\nTipo de veículo: 1 - Carro | 2 - Moto | 3 - Caminhão")
    tipo = ler_inteiro("Escolha o tipo: ")
    if tipo not in (1, 2, 3):
        print("Tipo inválido.")
        return

    placa = ler_texto("Placa: ").upper()
    modelo = ler_texto("Modelo: ")
    ano = ler_inteiro("Ano: ")
    diaria = ler_decimal("Valor da diária (R$): ")

    try:
        if tipo == 1:
            portas = ler_inteiro("Número de portas: ")
            veiculo = Carro(placa, modelo, ano, diaria, portas)
        elif tipo == 2:
            cilindradas = ler_inteiro("Cilindradas (cc): ")
            veiculo = Moto(placa, modelo, ano, diaria, cilindradas)
        else:
            capacidade = ler_decimal("Capacidade de carga (kg): ")
            veiculo = Caminhao(placa, modelo, ano, diaria, capacidade)
        locadora.cadastrar(veiculo)
        print("Veículo cadastrado com sucesso!")
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")


def listar_veiculos(locadora):
    """Exibe todos os veículos cadastrados."""
    veiculos = locadora.listar()
    print(f"\n{locadora}")
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return
    for numero, veiculo in enumerate(veiculos, start=1):
        print(f"{numero}. {veiculo}")


def buscar_veiculo(locadora):
    """Busca e exibe um veículo pela placa."""
    placa = ler_texto("\nPlaca a buscar: ")
    veiculo = locadora.buscar_por_placa(placa)
    if veiculo is None:
        print("Veículo não encontrado.")
    else:
        print(veiculo)


def calcular_alugueis(locadora):
    """Calcula o aluguel de todos os veículos com o mesmo método."""
    if not locadora.listar():
        print("\nNenhum veículo cadastrado.")
        return
    dias = ler_inteiro("\nQuantidade de dias de aluguel: ")
    if dias <= 0:
        print("A quantidade de dias deve ser maior que zero.")
        return
    print(f"\nAluguel por {dias} dia(s):")
    for veiculo, valor in locadora.simular_alugueis(dias):
        print(f"- {veiculo.placa} ({type(veiculo).__name__}): R$ {valor:.2f}")


def main():
    """Executa o menu até o usuário escolher sair."""
    locadora = Locadora("Locadora Prototipo")
    opcoes = {
        1: cadastrar_veiculo,
        2: listar_veiculos,
        3: buscar_veiculo,
        4: calcular_alugueis,
    }

    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        acao = opcoes.get(opcao)
        if acao is None:
            print("Opção inválida.")
        else:
            acao(locadora)


if __name__ == "__main__":
    main()