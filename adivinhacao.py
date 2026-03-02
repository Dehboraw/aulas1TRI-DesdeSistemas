#importação da biblioteca
import random

# Configurações do jogo
tentativas = 1
errou = True #necessário criar a variável para comparar, se for False, ...., se for True acontece alguma coisa.
sorteio_max = 10
tentativas_max = 3
numero = random.randint(0,sorteio_max)



while (tentativas <= tentativas_max):
    print("Tentativa:",tentativas)
    chute = int(input("Digite o seu chute (0 a 10): ")) 
    if chute == numero:
        print("Parabéns, você é o bonzão mesmo")
        errou = False
        break
        
    else:
        if chute > numero :
            print("O número é menor")
        else:
            print("O número é maior")
    tentativas = tentativas + 1

if errou == True:
    print("O número sorteado era:", numero)
print("### FIM DO JOGO ###")




