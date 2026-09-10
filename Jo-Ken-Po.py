import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura", "Agua",]
repeat = 0

while repeat <3:
    repeat += 1
    jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: ").capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")

    elif jogador or pc == "Agua":
        if pc or jogador == "Pedra":
            print("Água mole em Pedra e dura tanto bate até que fura, você venceu!")

    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    