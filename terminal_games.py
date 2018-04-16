import adivinha
import forca

print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("############ BEM VINDO A TERMINAL GAMES ###############")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

print("Escolha o jogo (1)-Adivinhação (2)-Forca")

escolha = int(input())

if escolha == 1 :
	adivinha.jogar()
elif escolha == 2:
	forca.jogar()
else :
	print("Não existe esse modo escolhido ;-;")
