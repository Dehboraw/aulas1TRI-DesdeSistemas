import random
palavras = ["KENNEDY", "ESCOLA", "PYTHON", "JAVASCRIPT", "POMBO"]
palavra = random.choice(palavras)
letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")
    
acertou = False
enforcou = False
limite_tentativas = 6 + len(palavra) # pareido com  .length do js
tentativa = 1

def mostrar_letrar_acertadas(): # DEF é função no python.
    for letra in letras_acertadas: 
        print(letra, end=" ")

print("Tente adivinhar a palavra secreta: ")
while(not acertou and not enforcou): #enquanto a pessoa não acertou.
    print("Você está na tentativa", tentativa, "de", limite_tentativas)
    mostrar_letrar_acertadas()
    print("")
    chute = input("Digite uma letra: ")
    indice = 0 
    for letra in palavra: #percorre cada intem(que eu chamei de letra), e compara se o chute é igual a uma das letras, e for, ele pega o [indice] que recebe essa letra
        if chute.upper() == letra:
            letras_acertadas[indice] = letra
        indice = indice + 1
    
    if tentativa == limite_tentativas:
        print("Você perdeu :(\nA palavra era: ", palavra)
        enforcou = True

    if letras_acertadas.count("_") == 0:
        mostrar_letrar_acertadas()
        print("Parabéns, você acertou a palavra secreta!")
        acertou = True
    
    tentativa = tentativa + 1






#OPERADORES LÓGICOS
# E  => AND
#TABELA VERDADE 
#Quero fazer um suco de banana e maçã
# banana = true
# maçã = true
#    E             OU
# V V = V        v v = v
# V F = F        v f = v
# F V = F        f v = f
# F F = F        f f = f
