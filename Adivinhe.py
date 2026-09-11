import random

print ("Adivinhe um número de 1 à 10, vamos lá?!")

pc = random.randint(1, 10)
chances = 3
opcoes = ["1", "2", "3", "4", "5","6", "7", "8", "9", "10"]

while chances > 0:
    chances -= 1
    jogador = int(input("Escolha um número de 1 à 10: "))

    if jogador != pc:
        print ("Você errou, você ainda tem",chances,"chances!")
        continue
    elif jogador == pc:
        print ("Você acertou! O número escolhido era : ",pc)
        break
    else:
        print ("Suas chances acabaram :(, o número correto era" ,pc)
        break

