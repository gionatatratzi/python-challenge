import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
prod = num1 * num2

quiz = int(input("Quanto fà " + str(num1) + " per " + str(num2) + ": "))

if quiz == prod:
    print("Bravo!")
else:
    print("Sbagliato: la risposta è " + str(prod))