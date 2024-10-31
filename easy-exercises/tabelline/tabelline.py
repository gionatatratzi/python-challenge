import random

scelta = str(input("Livello facile o difficile (F/D): "))

if scelta == 'D':
    i = 0

    for c in range(10):
        n = random.randint(1, 15) 
        m = random.randint(1, 15)

        domanda = float(input("Quanto fà " + str(n) + " X " + str(m) + " : "))
        risposta = n * m

        if domanda == risposta:
            i += 1

else:
    i = 0

    for c in range(10):
        n = random.randint(1, 10)
        m = random.randint(1, 10)

        domanda = float(input("Quanto fà " + str(n) + " X " + str(m) + " : "))
        risposta = n * m

        if domanda == risposta:
            i += 1

print("Risposte esatte = " + str(i))

