nome = str(input("Inserire il nome: "))
sesso = str(input("Inserire il sesso (M=maschio, F=femmina): "))
eta = int(input("Inserire l'età: "))

if sesso == 'M':
    if eta < 18:
        print("Caro " + str(nome) + ", sei troppo piccolo per questo programma")
    else:
        print("Gentile Sig. " + nome + ", benvenuto in questo programma")
elif sesso == 'F':
    if eta < 18:
        print("Cara " + str(nome) + ", sei troppo piccola per questo programma")
    else:
        print("Gentile Sig.ra " + nome + ", benvenuta in questo programma")