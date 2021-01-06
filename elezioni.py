print ("elezioni ballottaggio")
x = int(input("voti ricevuti del primo candidato:"))
y = int(input("voti ricevuti del secondo candidato:"))
z = x + y
d = (x/z)*100
u = (y/z)*100
print ("la percentuale del primo candidato è", d,"%")
print ("la percentuale del secondo candidato è", u,"%")
if d > u:
    print ("vince il primo candidato!")
if u > d:
    print ("vince il secondo candidato!")
if d == u:
    print ("i due candidati pareggiano")
