import random
import os

def jogar():
    os.system('cls')
    print("")
    print("/*--------------------------------------*/")
    print("Bem Vindo ao Jogo de Adivinhação!!")
    print("/*--------------------------------------*/")
    print("")

    print("Escolha a dificulda (1)-Facil (2)-Medio (3)-Dificil")

    escolha = int(input())
    pontos = 1000

    if escolha == 1:
        total_de_tentativas = 20
    elif escolha == 2:
        total_de_tentativas = 10
    elif escolha == 3:
        total_de_tentativas = 5
    else :
        print("")
        print("Escolheu dificuldade INSANA voce so tem uma tentativa")
        total_de_tentativas = 1

    nro_secreto = random.randrange(1, 101)


    for rodada in range(1, total_de_tentativas + 1):
        print("")
        print("Rodada {} de {}!!!" .format(rodada, total_de_tentativas))
        chute = input("Digite um nro de 1 a 100: ")

        chute = int(chute)

        nro_invalido = chute < 1 or chute > 100

        if nro_invalido:
            print("O nro digitada é invalido")
            continue

        igual           = nro_secreto == chute
        chute_foi_menor = chute < nro_secreto
        chute_foi_maior = chute > nro_secreto

        if (igual):
            print("Voce acertou!!")
            break
        else:
            if(chute_foi_maior):
                print("Voce errou pra cima !!!")
            elif(chute_foi_menor):
                print("Voce errou pra baixo !!!")
            pontos_perdidos = abs(nro_secreto - chute)
            pontos -= pontos_perdidos


    print("Voce fez {} pontos!!!" .format(pontos))

    print("")
    print("-----------------")
    print("    FIM DO JOGO    ")
    print("-----------------")

if __name__ == "__main__":
    jogar()
