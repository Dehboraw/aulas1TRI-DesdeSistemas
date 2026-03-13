palavra = "KENNEDY" 
letras_acertadas = ["_", "_", "_", "_" ,"_" , "_" , "_"]
acertou = False

def mostrar_letrar_acertadas(): # DEF é função no python.
    for letra in letras_acertadas: 
        print(letra, end=" ")


print("Tente adivinhar a palavra secreta: ")
while(not acertou): #enquanto a pessoa não acertou.
    mostrar_letrar_acertadas()

    print("")
    chute = input("Digite uma letra: ")
    indice = 0 #começa a partir do indice zero porque ele é o primeiro da lista.
    for letra in palavra: #percorre cada intem(que eu chamei de letra), e compara se o chute é igual a uma das letras, e for, ele pega o [indice] que recebe essa letra
        if chute.upper() == letra:
            letras_acertadas[indice] = letra
        indice = indice + 1
    
    if letras_acertadas.count("_") == 0:
        mostrar_letrar_acertadas()
        print("Parabéns, você acertou a palavra secreta!")

        acertou = True
