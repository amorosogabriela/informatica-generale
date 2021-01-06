print ("veicoli")
lista_v = []
count = True
x = 0
y = 0
t = 0
while count == True:
    x += 1
    y += 1
    print("veicoli entrati nel casello autostradale durante il giorno", x,"?")
    veicoli = int(input())
    lista_v.append(veicoli)

    if y == 3:
        s = int(input("desideri uscire dal casello autostradale? per uscire scrivi 0, altrimenti scrivi 1:"))
        y = 0
        if s == 0:
            count = False
        else:
            pass
for i in lista_v:
    t += i
print("in", x,"giorni, sono transitati", t, "veicoli")
