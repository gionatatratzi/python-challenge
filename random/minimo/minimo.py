import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

print("Ho generato i numeri: " + str(n1) + ", " + str(n2) + " e " + str(n3))

if n1 < n2 and n1 < n3:
    print("Il minimo è " + str(n1))
elif n2 < n1 and n2 < n3:
    print("Il minimo è " + str(n2))
elif n3 < n1 and n3 < n2:
    print("Il minimo è " + str(n3))
