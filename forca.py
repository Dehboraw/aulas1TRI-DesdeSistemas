import random
#Menu do jogo
while True:
    print("------------------------------------")
    print("Escolha um dos seguintes temas para jogar forca: ")
    print("1 - ANIMAIS")
    print("2 - ESCOLA ")
    print("3 - PAÍSES")
    print("4 - SAIR")
    print("------------------------------------")
    opcao = int(input("Digite a opção desejada (1 a 4): "))
    palavras = []
   
    if opcao == 1:
        arquivo = open("palavrasAnimais.txt", "r")
        print("------------------------------------")
        print("Selecionado o tema de ANIMAIS.")

    elif opcao == 2:
        arquivo = open("palavrasEscola.txt", "r")
        print("------------------------------------")
        print("Selecionado o tema de ESCOLA.")

    elif opcao == 3:
        arquivo = open("palavrasPaises.txt", "r")
        print("------------------------------------")
        print("Selecionado o tema de PAÍSES.")

    elif opcao == 4:
        print("Saiu do jogo")
        break # Sair do laço de repetição.
    else:
        arquivo = open("palavrasAnimais.txt", "r")
        print("Opção inválida, selecionado tema ANIMAIS automaticamente")


    for linha in arquivo:
        palavras.append(linha.strip())
    palavra = random.choice(palavras)

    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")

    acertou = False
    enforcou = False
    limite_tentativas = 6 + len(palavra) 
    tentativa = 1

    def mostrar_letrar_acertadas(): 
        for letra in letras_acertadas: 
            print(letra, end=" ")

    print(palavra)
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
