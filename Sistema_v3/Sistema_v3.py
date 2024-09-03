from abc import ABC, abstractmethod
from datetime import datetime


        self.saldo = 0
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f}  -  Data:  {datetime.now()}")
            return True

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}  -  Data:  {datetime.now()}")
            return True
        else:
            print("O valor do depósito deve ser positivo.")
            return False

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def exibir_extrato(self):
        print("======================== Extrato ======================== ")
        print(f"Conta {self.numero}: - Cliente: {self.cliente.nome}")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            self.historico.exibir()
        self.exibir_saldo()


class ContaCorrente(Conta):
    """Classe para representar uma conta corrente."""

    def __init__(self, agencia, numero, cliente, limite_saque=500, limite_saques_diarios=3):
        super().__init__(agencia, numero, cliente)
        self.limite_saque = limite_saque
        self.limite_saques_diarios = limite_saques_diarios
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
            return False
        elif valor > self.limite_saque:
            print("Valor do saque excede o limite de saque.")
            return False
        else:
            sucesso = super().sacar(valor)
            if sucesso:
                self.saques_realizados += 1
            return sucesso


class Transacao(ABC):
    """Classe abstrata para representar uma transação."""

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    """Classe para representar a transação de saque."""

    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)


class Deposito(Transacao):
    """Classe para representar a transação de depósito."""

    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)


# Funções para interagir com o sistema bancário
clientes = []
contas = []

def criar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente (somente números): ")
    endereco = input("Endereço do cliente: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")

    if any(cliente.cpf == cpf for cliente in clientes):
        print("CPF já cadastrado para outro cliente.")
        return

    cliente = PessoaFisica(nome, cpf, endereco, data_nascimento)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    agencia = "0001"
    numero = len(contas) + 1
    conta = ContaCorrente(agencia, numero, cliente)
    contas.append(conta)
    print(f"Conta criada com sucesso! Número: {numero}, Agência: {agencia}")

def listar_contas():
    for conta in contas:
        print(f"Agência: {conta.agencia}, Número: {conta.numero}, Cliente: {conta.cliente.nome}")

def depositar():
    numero_conta = int(input("Informe o número da conta para depósito: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta is None:
        print("Conta não encontrada.")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    transacao.registrar(conta)

def sacar():
    numero_conta = int(input("Informe o número da conta para saque: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta is None:
        print("Conta não encontrada.")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    transacao.registrar(conta)

def exibir_extrato():
    numero_conta = int(input("Informe o número da conta para exibir o extrato: "))
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)

    if conta is None:
        print("Conta não encontrada.")
        return

    conta.exibir_extrato()


# Menu do sistema bancário
def main():
    while True:
        print("\n========== MENU ==========")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Nova Conta")
        print("[5] Listar Contas")
        print("[6] Novo Usuário")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            criar_conta()
        elif opcao == "5":
            listar_contas()
        elif opcao == "6":
            criar_cliente()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

