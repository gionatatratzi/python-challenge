r = 0
n = 0

n = int(input("Inserisci una sequenza di numeri, uno per linea (0 per terminare): "))
r = n

if n == 0:
    print("La somma dei numeri inseriti e': 0")
else:
    while n > 0:
        n = int(input("Inserisci una sequenza di numeri, uno per linea (0 per terminare): "))
        r = r + n

        if n == 0:
            print("La somma dei numeri inseriti e': " + str(r))
            break

