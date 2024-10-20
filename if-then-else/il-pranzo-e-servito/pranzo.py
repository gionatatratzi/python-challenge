num = int(input("Inserisci il numero del tavolo: "))
pizza = str(input("Inserisci il tipo di pizza (M = Margherita, N = Napoli): "))
dolce = str(input("Inserisci il tipo di dolce (T = Tiramisù, S = Sorbetto): "))

print("\nConto del tavolo " + str(num) + "\n")

if pizza == 'M' and dolce == 'T':
     print("1 Pizza Margherita: 5 EUR")
     print("1 Tiramissù: 4 EUR")
elif pizza == 'M' and dolce == 'S':
     print("1 Pizza Margherita: 5 EUR")
     print("1 Sorbetto: 3 EUR")
elif pizza == 'N' and dolce == 'T':
     print("1 Pizza Napoli: 6 EUR")
     print("1 Tiramisù: 4 EUR")
elif pizza == 'N' and dolce == 'S':
     print("1 Pizza Napoli: 6 EUR")
     print("1 Sorbetto: 3 EUR")