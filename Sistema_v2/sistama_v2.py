from datetime import datetime
import  textwrap

# Constantes
AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Funções do sistema bancário

def verificar_cpf(cpf):
    return any(usuario["cpf"] == cpf for usuario in usuarios)

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    
    if verificar_cpf(cpf):
        print("Usuário com este CPF já cadastrado.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = localizar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Não é possível criar conta.")

def localizar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def listar_contas():
    if contas:
        for conta in contas:
            linha = f"""\
                Agência: {conta['agencia']}
                Conta: {conta['numero_conta']}
                Titular:{conta['usuario']['nome']}
            """
            print("="* 80)
            print(textwrap.dedent(linha))
    else:
        print("Não há contas cadastradas.")1

def depositar(saldo, valor, /, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido. Tente novamente com um valor positivo.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Valor de saque inválido. Tente novamente com um valor positivo.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido. Tente novamente amanhã.")
    elif valor > limite:
        print(f"Limite máximo por saque é de R$ {limite:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, extrato):
    print("\n================ Extrato ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}\n")
    print("\n================ EXTRATO ================")

def executar_deposito(saldo, extrato):
    valor = float(input("Digite o valor para depósito: R$ "))
    saldo, extrato = depositar(saldo, valor, extrato)
    return saldo, extrato

def executar_saque(saldo, extrato, numero_saques):
    valor = float(input("Digite o valor para saque: R$ "))
    saldo, extrato, numero_saques = sacar(
        saldo=saldo, valor=valor, extrato=extrato, 
        limite=LIMITE_VALOR_SAQUE, numero_saques=numero_saques, 
        limite_saques=LIMITE_SAQUES
    )
    return saldo, extrato, numero_saques

def executar_extrato(saldo, extrato):
    exibir_extrato(saldo, extrato)

def main():
    saldo = 0.0
    extrato = []
    numero_saques = 0

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
            saldo, extrato = executar_deposito(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = executar_saque(saldo, extrato, numero_saques)

        elif opcao == "3":
            executar_extrato(saldo, extrato)

        elif opcao == "4":
            criar_conta()

        elif opcao == "5":
            listar_contas()

        elif opcao == "6":
            criar_usuario()

        elif opcao == "0":
            print("Saindo do sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
