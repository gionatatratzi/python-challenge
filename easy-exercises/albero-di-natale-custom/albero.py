def stampa_albero_natale():
    # Chiede all'utente di inserire un'altezza tra 1 e 20
    altezza = int(input("Inserisci l'altezza dell'albero (tra 1 e 20): "))

    # Controlla che l'altezza sia nel range richiesto
    if altezza < 1 or altezza > 20:
        print("Errore: l'altezza deve essere compresa tra 1 e 20.")
        return

    # Genera l'albero riga per riga
    for i in range(altezza):
        # Calcola il numero di spazi a sinistra per centrare l'albero
        spazi = altezza - i - 1
        # Calcola il numero di asterischi per la riga attuale
        asterischi = 2 * i + 1

        # Stampa gli spazi e gli asterischi per la riga corrente
        print(" " * spazi + "*" * asterischi)


# Avvia il programma
stampa_albero_natale()
