class Banco:
    def __init__(self):
        self.saldo = 0.0  # Saldo inicial da conta
        self.extrato = []  # Lista para armazenar transações
        self.saques_diarios = 0  # Contador de saques diários

    def depositar(self, valor):
        """Função para depositar um valor na conta."""
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Tente novamente com um valor positivo.")

    def sacar(self, valor):
        """Função para sacar um valor da conta."""
        if valor <= 0:
            print("Valor de saque inválido. Tente novamente com um valor positivo.")
            return
        
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido. Tente novamente amanhã.")
            return

        if valor > 500:
            print("Limite máximo por saque é de R$ 500,00.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return

        # Realizar o saque
        self.saldo -= valor
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        self.saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def visualizar_extrato(self):
        """Função para exibir o extrato da conta."""
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n=========== Extrato ===========")
            for item in self.extrato:
                print(item)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


def main():
    banco = Banco()

    while True:
        print("\n--- Sistema Bancário ---")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[0] Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: R$ "))
            banco.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: R$ "))
            banco.sacar(valor)
        elif opcao == "3":
            banco.visualizar_extrato()
        elif opcao == "0":
            print("Saindo do sistema bancário. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
