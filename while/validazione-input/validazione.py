n = str(input("Inserisci il tuo anno di nascita: "))

if n >= '1900' and n <= '2021':
       print("Grazie. Il tuo anno di nascita e' il " + str(n))
else:
    while n < '1900' or n > '2021':
        m = str(input("Errore: l'anno deve essere compreso tra il 1900 e il 2021. Riprova: "))

        if m >= '1900' and m <= '2021':
            print("Grazie. Il tuo anno di nascita e' il " + str(m))
            break
