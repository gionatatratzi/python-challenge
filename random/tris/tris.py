import random

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)

s1 = random.randint(0, 3)
s2 = random.randint(0, 3)
s3 = random.randint(0, 3)
s4 = random.randint(0, 3)

print("Carta1: " + str(n1) + " di " + str(s1))
print("Carta2: " + str(n2) + " di " + str(s2))
print("Carta3: " + str(n3) + " di " + str(s3))
print("Carta4: " + str(n4) + " di " + str(s4))

if (n1 == n2 == n3) or (n1 == n2 == n4) or (n1 == n3 == n4) or (n2 == n3 == n4):
    print("Tris!")
else:
    print("Hai perso")