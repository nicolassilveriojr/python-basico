while True:
    try:
        idade = int(input("Digita sua idade:"))
        if idade <=0:
            print("A idade deve ser maior que zero.")
        else:
            break
    except ValueError:
        print("Digiter apenas numeros inteiros.")

print("Idade cadastrada:", idade)