import random

numero = random.randint(1, 10)
seme = random.randint(0, 3)

if seme == 0:
    s = "Cuori"
elif seme == 1:
    s = "Quadri"
elif seme == 2:
    s = "Fiori"
elif seme == 3:
    s = "Picche"

print("Carta: " + str(numero) + " di " + str(s))

if numero == 7:
    print("Hai vinto!")
else:
    print("Hai perso!")