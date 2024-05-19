menu = """
SERVIÇOS DISPONÍVEIS:

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

Informe a opção que deseja consultar
==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    servico = int(input(menu))

    if servico == 1:
        valor_saque = float(input("Informe o valor do saque: "))
        print(valor_saque)

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saque diário excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif servico == 2:
        valor_deposito = float(input("Insira o valor de depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Recebemos o depósito de: R$ {valor_deposito:.2f}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif servico == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif servico == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
