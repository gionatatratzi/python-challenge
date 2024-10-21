import random

num = random.randint(1, 5)

ut = int(input("Inserisci un numero tra 1 e 5: "))

if ut < 1 or ut > 5:
    print("ERRORE")
else:
    if ut == num:
        print("Hai vinto")
    else:
        print("Hai perso")
