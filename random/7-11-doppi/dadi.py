import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Lancio di dadi: " + str(dado1) + " e " + str(dado2))

if (dado1 == dado2) or (dado1 + dado2 == 7) or (dado1 + dado2 == 11):
    print("Hai vinto")
else:
    print("Hai perso")