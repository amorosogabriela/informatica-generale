lista_nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
lista_capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
print("NAZIONI E CAPITALI")
print("inserisci il nome di uno di questi stati: Italia, Francia, Germania, Spagna, Inghilterra, Grecia, Turchia e Portogallo, scoprirai così la sua capitale. ")

while True:
    opzione = input("scegli una nazione: ").capitalize()
    numero = lista_nazioni.index(opzione)
    if opzione in lista_nazioni:
        print("la capitale di", opzione, "è: ", lista_capitali[numero])
        opzione2 = int(input("nel caso volessi scoprirne un'altra... digita 0 per inserirne una nuova e 1 per uscire:\n"))
        if opzione2 == 1:
            break
        elif opzione2 == 0:
            print("inseriscine una nuova ")
        else:
            print("numero non corretto")
            break
    elif opzione not in lista_nazioni:
        print("questa nazione non è presente in elenco, provane un'altra ")
    else:
        pass
