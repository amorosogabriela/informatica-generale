print("LISTA PAZIENTI")

pazienti = []
while True:
    paziente = input("scrivere il nome del paziente, per bloccare il programma digita stop: ")
    paziente = paziente.capitalize()
    if paziente == "Stop":
        break
    else: 
        pazienti.append(paziente)
primo = pazienti.pop(0)
print("il primo paziente in lista è", primo)
while len(pazienti) >0:
    input("premi invio per scoprire il nome del prossimo paziente")
    paziente = pazienti.pop(0)
    print("il paziente seguente è", paziente)
