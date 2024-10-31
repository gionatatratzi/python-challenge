numero = int(input("Quanti spettatori ci sono: "))
index, n_adulti, n_bambini, n_over65, prezzo = 0, 0, 0, 0, 0
eta = dict()
vip = dict()

for i in range(numero):
    index += 1
    eta[i] = int(input(str(index) + ") Quanti anni hai: "))
    vip[i] = str(input(str(index) + ") Desideri il posto vip (S/N): "))

    if eta[i] >= 18:
        n_adulti = n_adulti + 1

    if eta[i] < 18:
        n_bambini = n_bambini + 1

    if eta[i] > 65:
        n_over65 = n_over65 + 1

for c in range(numero):
    if eta[c] >= 13 and eta[c] <= 64:
        prezzo = prezzo + 8

        if vip[c] == 'S':
            prezzo = prezzo + 1

    elif eta[c] <= 12:
        prezzo = prezzo + 8
        prezzo = prezzo / 2

        if vip[c] == 'S':
            prezzo = prezzo + 1

    elif eta[c] >= 65:
        prezzo = prezzo + 8
        prezzo = prezzo / 2

    elif n_adulti >=2 and n_bambini >= 2:
        prezzo = prezzo + 8
        prezzo = prezzo * 20 / 100

    elif n_over65 >= 4:
        prezzo = prezzo + 8
        prezzo = prezzo * 20 / 100

print("Il prezzo totale da pagare è " + str(prezzo) + " EURO")
