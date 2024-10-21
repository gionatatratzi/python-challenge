num = int(input("Inserire un numero intero: "))
n = num
s = 0

while num > 0:
    s = s + num
    num = num - 1

print("La somma dei numeri da 1 a " + str(n) + " è " + str(s))