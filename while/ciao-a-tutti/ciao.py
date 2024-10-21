l = 0

while True:
    nome = str(input("Chi sei? "))

    if l == 0 and nome == 'nessuno':
        print("Benvenuto")
        break
    elif l != 0 and nome == 'nessuno':
        print("Benvenuti a tutti e " + str(l))
        break
    else:
        l = l + 1
        print("Ciao, " + str(nome))

