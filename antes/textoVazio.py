while True:
    nome = input("Digite seu nome: "). strip()

    if nome == "":
        print("O nome não pode ser vazio. Por favor, digite um nome válido.")
    else:
        break

print("Nome registrado:", nome)