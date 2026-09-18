opcao = 0
nota = 0

while opcao != 4:
    print ("===Ambiente de Notas do Aluno===")
    print ("1 - Informar nota")
    print ("2 - Consultar situação do aluno")
    print ("3 - Sair")
    

    opcao = int(input("Escolha a opção desejada: "))

    if opcao == 1:
        nota = int(input("Informe sua nota: ")) 
        print ("Nota registrada com sucesso!") 

    elif opcao == 2:
        nota >= 7
        print ("Sua nota é " ,nota, "e você está aprovado!")

    elif opcao == 2:
        nota >= 5 and opcao < 7
        print ("Sua nota é " ,opcao, "e você está em recuperação!")    

    elif opcao == 2:
        nota < 5
        print ("Sua nota é " ,opcao, "e você está reprovado!")

    elif opcao == 3:
        break

    else:
        ("Valor inválido, tente novamente")
        continue
        
    