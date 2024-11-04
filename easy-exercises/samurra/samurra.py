import random

nome_utente = str(input("Inserire il nome utente: "))
punti_utente = 0
punti_computer = 0
mano = 0
mano_utente = 0
giocata_utente = 0

while mano < 16:
    mano += 1
    mano_utente = 0
    giocata_utente = 0

    mano_computer = random.randint(1, 5)
    giocata_computer = random.randint(2, 10)

    print("**************************************************************************************")
    print("MANO: " + str(mano))

    while mano_utente > 5 or mano_utente < 1:
        mano_utente = int(input("Inserire la mano (1/5): "))

    while giocata_utente < 2 or giocata_utente > 10:
        giocata_utente = int(input("Inserire la giocata (2/10): "))

    print("Mano Computer: " + str(mano_computer) + "\tGiocata Computer: " + str(giocata_computer))

    if giocata_computer == mano_computer + mano_utente:
        punti_utente += 1

    if giocata_utente == mano_computer + mano_utente:
        punti_computer += 1

    if punti_computer == 3:
        break

    if punti_utente == 3:
        break

print("\n**************************************************************************************")
print("Punteggio " + str(nome_utente) + ": " + str(punti_utente))
print("Punteggio Computer: " + str(punti_computer))

if punti_computer == punti_utente:
    print("Hanno vinto in parità " + str(nome_utente) + " e il Computer")

elif punti_utente > punti_computer:
    print("Ha vinto " + str(nome_utente))

elif punti_computer > punti_utente:
    print("Ha vinto il Computer")