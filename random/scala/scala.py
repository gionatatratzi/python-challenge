import random

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)

s1 = random.randint(0, 3)
s2 = random.randint(0, 3)
s3 = random.randint(0, 3)

print("Carta1: " + str(n1) + " di " + str(s1))
print("Carta2: " + str(n2) + " di " + str(s2))
print("Carta3: " + str(n3) + " di " + str(s3))

if (n1 == n2 - 1 == n3 - 2) and (s1 != s2 != s3):
    print("Scala")
elif (n1 == n2 - 1 == n3 - 2) and (s1 == s2 == s3):
    print("Scala reale")
else:
    print("Hai perso")