import random
import os

def jogar ():

    os.system('clear')
    display_abertura()

    palavras = abri_arquivo()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].lower()
    lista_da_palavra = ["_" for letra in palavra_secreta]
    tentativas = 7

    enforcou = False
    acertou = False

    print("")
    print("A palavra e:")
    print(lista_da_palavra)
    print("")


    while (not enforcou and not acertou):
        chute = input("Digite uma letra:")
        chute = chute.strip()
        chute = chute.lower()

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    lista_da_palavra[index] = chute
                index += 1

            print(lista_da_palavra)
            print("")

        else:
            print("")
            print("Voce errou !!!")
            tentativas -= 1
            desenha_forca(tentativas)

        enforcou = tentativas == 0
        acertou = "_" not in lista_da_palavra

    if(acertou):
        acertou_display()
    else:
        errou(palavra_secreta)

    display_final()


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def acertou_display():
    print("")
    print("Voce acertou o enigma!!!!!!!")
    print("")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def errou(palavra_secreta):
    print("")
    print("Voce errou o enigma !!!!!!!!")
    print("")
    print("A palavra secreta era {} " .format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def display_final():
    print("")
    print("/*---------------------------*/")
    print("======== FIM DO JOGO ==========")
    print("/*---------------------------*/")
    print("")


def display_abertura():
    print("")
    print("/*--------------------------------------*/")
    print("====== BEM VINDO AO JOGO DA FORCA ========")
    print("/*--------------------------------------*/")
    print("")

def abri_arquivo():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    return palavras


if __name__ == "__main__" :
    jogar()
