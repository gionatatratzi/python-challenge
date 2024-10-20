mese = int(input("Inserisci il mese: "))
giorno = int(input("Inserisci il giorno: "))

if mese == 1 and (giorno >= 1 and giorno <= 28):
     print("Data corretta")
elif (mese == 9 or mese == 4 or mese == 6 or mese == 9) and (giorno >= 1 and giorno <= 30):
     print("Data corretta")
elif (mese == 2 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 11 or mese == 12)\
     and (giorno >= 1 and giorno <= 31):
     print("Data corretta")
else:
     print("Data errata")