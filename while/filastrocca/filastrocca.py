num = int(input("Inserire un numero: "))
i = 1

while num > 0:
    if i == 1:
        print(str(i) + " elefante si dondolava giu' dal filo di una ragnatela, e trovando il gioco interessante, ando' a chiamare un altro elefante.")
    else:
        print(str(i) + " dondolavano giu' dal filo di una ragnatela, e trovando il gioco interessante, andarono a chiamare un altro elefante.")
    i = i + 1
    num = num - 1