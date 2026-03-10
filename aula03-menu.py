# Menu de opções usando o terminal
while True:
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Opção 4")
    print("5 - SAIR")
    opcao = int(input("Digite a opção desejada (1 a 4): "))

    if opcao == 1:
        print("Selecionado opção 1")
    elif opcao == 2: #SENÃO SE : SENÃO acontecer tal opção, e SE acontecer a próxima condição
        print("Selecionado opção 2")
    elif opcao == 3:
        print("Selecionado opção 3")
    elif opcao == 4:
        print("Selecionado opção 4")
    elif opcao == 5:
        break # Sair do laço de repetição.
    else:
        print("--------------------------------------------")
        print("Opção inválida, precisa ser um número de 1 a 4")
        #opcao = int(input("Digite a opção desejada (1 a 4): "))   #não funciona, porque se o usuário selecionar outra opção "errada" de novo, ele não volta   

        


#CRIE UMA OPÇÃO PARA O USUÁRIO SAIR DO SISTEMA (break)