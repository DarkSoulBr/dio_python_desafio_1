menu = """
Bem vindo a sua Conta, escolha a opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_VALOR = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "s":

        if numero_saques >= LIMITE_SAQUES:
            print(f"Você já realizou o limite diário de {LIMITE_SAQUES} saques")
        else:
            valor = float(input("Informe o valor do Saque: "))
            if valor > 0 and valor > saldo:
                print(f"Saque de R$ {valor:.2f} Excedeu o saldo total de R$ {saldo:.2f}")
            elif valor > 0 and valor > LIMITE_VALOR:
                print(f"Exceu o limite por saque de R$ {LIMITE_VALOR:.2f}")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")    

    elif opcao == "e":

        cabecalho = " Extrato "        
        print("\n" + cabecalho.center(30, "#"))        
        print("\n")
        print("Sem movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n")
        print("".center(30, "#"))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
