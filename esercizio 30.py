print("rappresentazione in decimale di un numero binario")
lunghezza = int(input("inserisci numero delle cifre binarie: "))
tot = 0
for n in range (lunghezza):
    num = int(input("disponi le cifre partendo da destra: "))
    valore = (num*2**n)
    tot += valore
print(tot)
