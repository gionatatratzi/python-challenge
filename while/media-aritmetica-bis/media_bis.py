contatore = 0

voto = int(input("Inserisci una sequenza di voti, uno per linea: "))
contatore += 1
media = voto
somma = voto

while True:
    if voto != 0 and (voto < 18 or voto > 30):
        break
    elif voto == 0:
        print("La media dei voti e': " + str(media))
        break
    else:
        voto = int(input("Inserisci una sequenza di voti, uno per linea: "))

        if voto != 0:
            contatore += 1
            somma = somma + voto
            media = somma / contatore
