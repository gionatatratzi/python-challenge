cono_coppetta = int(input("Cono (0) o coppetta (1): "))

g_1 = 2.5
g_2 = 3
g_3 = 3.5
cioc = 0.5

if cono_coppetta == 0:
    gusti = int(input("Gusti? (max 3): "))

    if gusti <= 0 or gusti > 3:
        print("ERRORE")

    agg = str(input("Aggiunta di cioccolato (s/n): "))

    if agg == 'n':
        if gusti == 1 :
            print("Totale: " + str(g_1) + " EUR")
        elif gusti == 2:
            print("Totale: " + str(g_2) + " EUR")
        elif gusti == 3:
            print("Totale: " + str(g_3) + " EUR")
    elif agg == 's':
        if gusti == 1 :
            print("Totale: " + str(g_1 + cioc) + " EUR")
        elif gusti == 2:
            print("Totale: " + str(g_2 + cioc) + " EUR")
        elif gusti == 3:
            print("Totale: " + str(g_3 + cioc) + " EUR")

elif cono_coppetta == 1:
    gusti = int(input("Gusti? (max 3): "))

    if gusti <= 0 or gusti > 3:
        print("ERRORE")

    if gusti == 1:
        print("Totale: " + str(g_1) + " EUR")
    elif gusti == 2:
        print("Totale: " + str(g_2) + " EUR")
    elif gusti == 3:
        print("Totale: " + str(g_3) + " EUR")




# 1 gusto: 2.5 EUR
# 2 gusti: 3 EUR
# 3 gusti: 3.5 EUR
# aggiunta di cioccolato: 0.50 EUR (disponibile solo sul cono)