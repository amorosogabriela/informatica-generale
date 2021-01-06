print("escurisone termica città")
nomi = []
listamax = []
listaminima = []
escursione = []
x = True
città = 0
temperaturamax = 0
temperaturamin = 0
escursione_temperatura= 0
print("qual è il valore dell'escursione termica da prefissare? ")
valore_prefissare = int(input())

while x == True:
    città += 1
    temperaturamax += 1
    temperaturamin += 1
    escursione_temperatura += 0
    print("nome città", città,"?")
    nomi2 = input()
    nomi.append(nomi2)
    print("temperatura max segnata oggi a", nomi2,"? ")
    temperatura1 = int(input())
    listamax.append(temperatura1)
    print("temperatura min segnata oggi a", nomi2,"? ")
    temperatura2 = int(input())
    listaminima.append(temperatura2)
    escursione_termica = temperatura1 - temperatura2
    if escursione_termica > valore_prefissare:
         escursione.append(escursione_termica)
    else:
         pass
    y = int(input("nel caso tu abbia finito l'elenco di città puoi terminare premento 0, se vuoi continuare premi un altro comando casuale: "))
    if y == 0:
        x = False
    else:
        pass
    
escursione.reverse()
print("le escursioni termiche maggiori al valore prefissato sono:", escursione[:])
