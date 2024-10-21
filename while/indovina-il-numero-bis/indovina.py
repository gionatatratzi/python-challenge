import random

n = 10

while n > 0:
    r = random.randint(1, 10)
    i = int(input("Indovina il numero: "))

    if r == i:
        print("Hai vinto!")
    else:
        print("Hai sbagliato! riprova")

    n = n - 1