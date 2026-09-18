print ("Bem-vindo à calculadora!")

opcao = 0

while opcao != 5:
    print ("1 - Somar")
    print ("2 - Subtrair")
    print ("3 - Multiplicar")
    print ("4 - Dividir")
    print ("5 - Sair")

    opcao = int(input("Digite a opção que deseja usar: "))

    if opcao == 1:
        numero1 = float (input("Digite o 1º valor: "))
        numero2 = float(input("Digite o 2º valor: "))

        resultado = numero1 + numero2

        print ("O resultado é ",resultado,)
        break

    elif opcao == 2:
            numero1 = float (input("Digite o 1º valor: "))
            numero2 = float(input("Digite o 2º valor: "))
    
            resultado = numero1 - numero2
    
            print ("O resultado é ",resultado,)
            break

    elif opcao == 3:
            numero1 = float (input("Digite o 1º valor: "))
            numero2 = float(input("Digite o 2º valor: "))
    
            resultado = numero1 * numero2
    
            print ("O resultado é ",resultado,)
            break

    elif opcao == 4:
            numero1 = float (input("Digite o 1º valor: "))
            numero2 = float(input("Digite o 2º valor: "))
    
            resultado = numero1 / numero2
    
            print ("O resultado é ",resultado,)
            break

    else:
          print ("Você saiu!")
          break