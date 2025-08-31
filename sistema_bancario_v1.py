

print("""
     ███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗     ██████╗  █████╗ ███╗   ██╗ ██████╗██████╗ ██╗ ██████╗      ██████╗ ██████╗ ███╗   ███╗    ██████╗ ██╗   ██╗
     ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██║██╔═══██╗    ██╔════╝██╔═══██╗████╗ ████║    ██╔══██╗╚██╗ ██╔╝
     ███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║    ██████╔╝███████║██╔██╗ ██║██║     ██████╔╝██║██║   ██║    ██║     ██║   ██║██╔████╔██║    ██████╔╝ ╚████╔╝ 
     ╚═══ ██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║    ██╔══██╗██╔══██║██║╚██╗██║██║     ██╔══██╗██║██║   ██║    ██║     ██║   ██║██║╚██╔╝██║    ██╔═══╝   ╚██╔╝  
     ███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║    ██████╔╝██║  ██║██║ ╚████║╚██████╗██║  ██║██║╚██████╔╝    ╚██████╗╚██████╔╝██║ ╚═╝ ██║    ██║        ██║   
     ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝        ╚═╝   
     Bruno Molina                                                                                                                        Santander 2025 - Back-End com Python                                                                                                                                                   
      
""")

menu = """
[1] Débito
[2] Pix
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair
=> """

saldo = 0.0
extrato = ""


limite_debito = 50000
limite_pix = 5000
limite_saque = 1500

saques_debito = 0
saques_pix = 0
saques_comum = 0
LIMITE_SAQUES_DIARIO = 3

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(saldo, extrato, tipo, limite, contador_saques):
    try:
        valor = float(input(f"Informe o valor do saque ({tipo}): "))
        if valor <= 0:
            print("Operação falhou! Valor inválido.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print(f"Operação falhou! Valor excede o limite de R$ {limite:.2f}.")
        elif contador_saques >= LIMITE_SAQUES_DIARIO:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque ({tipo}): R$ {valor:.2f}\n"
            contador_saques += 1
            print(f"Saque de R$ {valor:.2f} ({tipo}) realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato, contador_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("========================================")

while True:
    opcao = input(menu).strip()
    
    if opcao == "1":  # Débito
        saldo, extrato, saques_debito = sacar(saldo, extrato, "Débito", limite_debito, saques_debito)
    elif opcao == "2":  # Pix
        saldo, extrato, saques_pix = sacar(saldo, extrato, "Pix", limite_pix, saques_pix)
    elif opcao == "3":  # Depositar
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "4":  # Saque comum
        saldo, extrato, saques_comum = sacar(saldo, extrato, "Saque", limite_saque, saques_comum)
    elif opcao == "5":  # Extrato
        exibir_extrato(saldo, extrato)
    elif opcao == "6":  # Sair
        print(r" _____________") 
        print(r"| Obrigado    |")
        print(r"| O sistema.  |")
        print(r"| Até mais!   |")
        print(r"|_____________|")
        print(r"  (\__/)||")
        print(r"  (•ㅅ•)||")
        print(r"  /    づ ")
        break
    else:
        print("Operação inválida! Selecione uma opção válida.")
