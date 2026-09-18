print ("Bem-vindo ao Caixa Eletrônico!")

opcao = 0
saldo = 2000
deposito = 0
saque = 0

while opcao != 4:
    print ("Escolha a opção desejada: ")
    print ("1 - Consultar saldo")
    print ("2 - Realizar depósito")
    print ("3 - Realizar saque")
    print ("4 - Encerrar")

    opcao = int(input("Opção "))

    if opcao == 1:
        saldo += deposito
        saldo -= saque
        print ("Seu saldo é de R$",saldo, "reais.")

    elif opcao == 2:
        deposito = int(input("Digite o valor que deseja depositar: "))
        print ("Depósito de ",deposito,"realizado com sucesso!")

    elif opcao == 3:
        saque = int(input("Digite o valor que deseja sacar: "))
        if saldo < saque:
            print ("Saldo insuficiente!")

        else:
            print ("Saque de ",saque," realizado com sucesso!")

    elif opcao == 4:
        print ("Você saiu!")
        break

    else:
        print ("Opção inválida!")
