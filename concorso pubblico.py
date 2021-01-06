print ("concorso pubblico")
l = input("qual è il nome del primo candidato?")
r = input("quel è il nome del secondo candidato?")
x = int(input("punteggio del primo candidato:"))
y = int(input("punteggio del secondo candidato:"))
if x > y :
    print("ordine decrescente del punteggio:", x, y)
if x < y :
    print("ordine decrescente del punteggio:", y, x)
list = [l,r]
list.sort()
print("in ordine alfabetico:", list)
