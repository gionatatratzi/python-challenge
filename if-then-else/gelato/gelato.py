d = input("la dimensione del gelato (P = Piccolo, G = Grande): ")
a = input("se si desidera l'aggiunta di panna (S = Sì, N = No): ")
g = input("se si desidera l'aggiunta di granella (S = Sì, N = No): ")

gp = 3 # Gelato piccolo: 3 EUR
gg = 5 # Gelato grande: 5 EUR
ap = 1 # Aggiunta di panna: 1 EUR
ag = 1 # Aggiunta di granella: 1 EUR
apg = 1.5 # Aggiunta di panna e granella: 1.5 EUR

if d == 'P' and a == 'S' and g == 'S':
    print("Totale: " + str(gp + ap + ag) + " EURO")
elif d == 'P' and a == 'S' and g == 'N':
    print("Totale: " + str(gp + ap) + " EURO")
elif d == 'P' and a == 'N' and g == 'S':
    print("Totale: " + str(gp + ag) + " EURO")
elif d == 'P' and a == 'N' and g == 'N':
    print("Totale: " + str(gp) + " EURO")
elif d == 'G' and a == 'S' and g == 'S':
    print("Totale: " + str(gg + ap + ag) + " EURO")
elif d == 'G' and a == 'S' and g == 'N':
    print("Totale: " + str(gg + ap) + " EURO")
elif d == 'G' and a == 'N' and g == 'S':
    print("Totale: " + str(gg + ag) + " EURO")
elif d == 'G' and a == 'N' and g == 'N':
    print("Totale: " + str(gg) + " EURO")