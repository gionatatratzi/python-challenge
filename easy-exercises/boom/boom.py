def gioco_boom():
    numero = 1

    while True:
        # Se il numero è multiplo di 7 o contiene il 7, si dovrebbe dire "Boom" (0 nel nostro caso)
        if numero % 7 == 0 or "7" in str(numero):
            risposta = input("Prossimo numero: 0\n")
        else:
            risposta = input(f"Prossimo numero: {numero}\n")

        # Controllo la risposta dell'utente
        if (numero % 7 == 0 or "7" in str(numero)) and risposta != "0":
            print("Hai perso!")
            break
        elif (numero % 7 != 0 and "7" not in str(numero)) and risposta != str(numero):
            print("Hai perso!")
            break

        # Passa al prossimo numero
        numero += 1


# Avvia il gioco
gioco_boom()
