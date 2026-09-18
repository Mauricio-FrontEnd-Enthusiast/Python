print ("Você pode votar em um dos 3 candidatos a seguir: Cebolinha, Baiconzito ou Fandango.")

opcao = 0
contarVotoCebola = 0
contarVotoBaiconzito = 0
contarVotoFandango = 0

while opcao != 4:
    print ("Escolha um candidato: ")
    print ("1 - Cebola")
    print ("2 - Baiconzinto")
    print ("3 - Fandango")
    print ("4 - Encerrar votação!")

    opcao = int(input("Digite a opção em que quer votar: "))

    if opcao == 1:
        contarVotoCebola += 1
        resultadoCebola = contarVotoCebola
        print ("Voto registrado para o Cebola")

    elif opcao == 2:
        contarVotoBaiconzito += 1
        resultadoBaiconzito = contarVotoBaiconzito
        print ("Voto registrado para o Baiconzito")

    elif opcao == 3:
        contarVotoFandango += 1
        resultadoFandango = contarVotoFandango
        print ("Voto registrado para o Fandango")

    elif opcao == 4:
        print ("Votação encerrada!")
        print ("RESULTADOS:")
        print ("Candidato Cebola obteve ",resultadoCebola, "votos!")
        print ("Candidato Baiconzito obteve ",resultadoBaiconzito, "votos!")
        print ("Candidato Fandango obteve ",resultadoFandango, "votos!")
        break

    else:
        print ("Opção inválida, tente novamente!")