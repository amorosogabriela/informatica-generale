lista_nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
lista_capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
dizionario = {}
numero = len(lista_nazioni)
for num in range(0, numero):
    dizionario[lista_nazioni[num]] = lista_capitali[num]

print("NAZIONI E CAPITALI")
print("inserisci il nome di uno di questi stati: Italia, Francia, Germania, Spagna, Inghilterra, Grecia, Turchia e Portogallo, scoprirai così la sua capitale. ")

while True:
    opzione = input("scegli una nazione: ").capitalize()
    if opzione in dizionario.keys():
        print("questa è la capitale:", dizionario[opzione])
        opzione2 = int(input("nel caso volessi scoprirne un'altra... digita 0 per inserirne una nuova e 1 per uscire:\n"))
        if opzione2 == 1:
            break
        elif opzione2 == 0:
            print("inseriscine una nuova")
        else:
            print("numero non corretto")
            break
    elif opzione not in dizionario.keys():
        print("questa nazione non è presente in elenco, provane un'altra ")
    else:
        pass
