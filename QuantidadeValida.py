while True:
    try:
        quantidade = int(input("digite a quantidade de itens: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que 0")
        else:
            break
    except ValueError:
        print("Ocorreu um erro inesperado. Por favor, tente novamente.")

print("Quantidade cadastrada:", quantidade)