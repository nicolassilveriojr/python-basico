while True:
    try:
        nota = float(input("Digite uma nota entre 0 a 10: "))

        if 0 <= nota <= 10:
            break
        else:
            print("A nota deve estar entre 0 e 10. ")
    except ValueError:
        print("digite um numero válido")

print ("Nota Registrada!", nota)