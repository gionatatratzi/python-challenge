import random

n6 = random.randint(0, 1)

if n6 == 1:
    dado = 6
else:
    dado = random.randint(1, 5)

print("Dado: " + str(dado))