import random

nome_utente = str(input("Inserire il nome utente: "))
punti_utente = 0
punti_computer = 0
turno = 0
giocata_utente = 0

while turno < 10:
    turno += 1
    giocata_utente = -1
    giocata_computer = random.randint(0, 2)

    print("**************************************************************************************")
    print("MANO: " + str(turno))

    while giocata_utente > 2 or giocata_utente < 0:
        giocata_utente = int(input("Inserire Carta = 0, Forbice = 1, Sasso = 2: "))

    if giocata_utente > giocata_computer:
        punti_utente += 1

    elif giocata_utente < giocata_computer:
        punti_computer += 1

print("\n**************************************************************************************")
print("Punteggio di " + str(nome_utente) + ": " + str(punti_utente))
print("Punteggio del Computer: " + str(punti_computer))

if punti_computer >= 3 and punti_utente >= 3:
    print("Hanno vinto in parità " + str(nome_utente) + " e il Computer")
elif punti_utente >= 3:
    print("Ha vinto " + str(nome_utente))
elif punti_computer >= 3:
    print("Ha vinto il Computer")