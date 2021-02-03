lista_nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
lista_capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
dizionario = {}
num = len(lista_nazioni)
for numero in range(0, num):
    dizionario[lista_nazioni[numero]] = lista_capitali[numero]
dizionario_2 = dict(zip(dizionario.values(), dizionario.keys()))

print("CAPITALI E NAZIONI")
print("inserisci il nome di una di queste capitali: Roma, Parigi, Berlino, Madrid, Londra, Atene, Ankara e Lisbona, scoprirai così la nazione corrispondente.")

while True:
    opzione = input("scegli una capitale: ").capitalize()
    if opzione in dizionario_2.keys():
        print("questa è la sua nazione: ", dizionario_2[opzione])
        opzione_2 = int(input("nel caso volessi scoprirne un'altra... digita 0 per inserirne una nuova e 1 per uscire:\n"))
        if opzione_2 == 1:
            break
        elif opzione_2 == 0:
            print("inseriscine una nuova")
        else:
            print("numero non corretto")
            break
    elif opzione not in dizionario_2.keys():
        print("questa capitale non è presente in elenco, provane un'altra ")
    else:
        pass
