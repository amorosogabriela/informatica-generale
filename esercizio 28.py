print("gara sportiva")
valori = []
print("se hai terminato rispondi 0 al punteggio")
while True:
    nome = input("nome dello studente: ")
    punteggio = int(input ("punti fatti? "))
    if punteggio == 0:
        break
    valori.append(punteggio)
print(max(valori))
