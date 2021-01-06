print("calcolo equazione di primo grado")
numero_a = int(input("scrivi il valore di a: "))
numero_b = int(input("scrivi il valore di b: "))
if numero_a == 0 and numero_b == 0:
    print("questa equazione risulta indeterminata")
elif numero_a != 0 and numero_b == 0:
    print("la soluzione di questa equazione è x=0")
elif numero_a == 0 and numero_b != 0:
    print("questa equazione risulta impossibile")
elif numero_a != 0 and numero_b != 0:
    print("la soluzione di questa equazione è x=-b/a")
