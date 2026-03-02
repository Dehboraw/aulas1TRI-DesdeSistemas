#importação da biblioteca
import random
# sorteio do número aleatório
numero = random.randint(0,10)
#TESTE
print(numero)
tentativas = 1
while (tentativas <= 3):
    print("Tentativa:",tentativas)
    chute = int(input("Digite o seu chute (0 a 10): ")) #conversão para número inteiro, pois o input recebe os dados do usuário como tipo str.
    if chute == numero:
        print("Parabéns, você é o bonzão mesmo")
        break #para o while, para o bloco do laço
    else:
        if chute > numero :
            print("O número é menor")
        else:
            print("O número é maior")

    tentativas = tentativas + 1
print("O número sorteado era:", numero)
print("### FIM DO JOGO ###")

# Dizer para o usuário se o número era maior ou menor.


