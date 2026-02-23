while True:
    print("Menu:")
    print("1. cadastra ")
    print("2. consultar ")
    print("3. Exit")

    opcao = input("escolha uma opção: ")

    if opcao == '1':
        print("Você selecionou a opção 1.")
    elif opcao == '2':
        print("Você selecionou a opção 2.")
    elif opcao == '3':
        print("Saindo do menu. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")