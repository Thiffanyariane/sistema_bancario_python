def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:
        servico = menu_servicos()

        if servico == 1:
            saldo, extrato = saque(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif servico == 2:
            saldo, extrato = deposito(saldo, extrato)
        
        elif servico == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif servico == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif servico == 5:
            listar_contas(contas)
        
        elif servico == 6:
            criar_usuario(usuarios)

        elif servico == 7:
            break

def menu_servicos():
    menu = """
    SERVIÇOS DISPONÍVEIS:

    [1] Saque
    [2] Depósito
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas 
    [6] Novo Usuário
    [7] Sair

    Informe a opção que deseja consultar
    ==> """
    return int(input(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Novo usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']}, C/c: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def saque(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor_saque = float(input("Informe o valor do saque: "))

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
    
    return saldo, extrato

def deposito(saldo, extrato, /):
    valor_deposito = float(input("Insira o valor de depósito: "))
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Recebemos o depósito de: R$ {valor_deposito:.2f}\n")
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

main()
