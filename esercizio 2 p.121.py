import math

def delta_calcolo(a, b, c):
    der = math.pow(b, 2) - 4 * a * c
    return der

def vertice_calcolo(a, b, c):
    delta = delta_calcolo(a, b, c)
    Xv = -(b/(2*a))
    Yv = -(delta/(4*a))
    return Xv, Yv

def fuoco_calcolo(a, b, c):
    delta = delta_calcolo(a, b, c)
    Xf = -(b/(2*a))
    Yf = (1 - delta)/(4*a)
    return Xf, Yf

def main():
    a = int(input("scrivi quanto vale a: "))
    b = int(input("scrivi quanto vale b: "))
    c = int(input("scrivi quanto vale c: "))

    opzione = int(input("dimmi cosa vorresti calcolare, premi 1 per sapere il vertice, 2 per il fuoco, se preferisci uscire premi 0 altrimenti premi 3 per sapere sia il vertice sia il fuoco: "))
    if opzione == 1:
        print(vertice_calcolo(a, b, c))
    elif opzione == 2:
        print(fuoco_calcolo(a, b, c))
    elif opzione == 0:
        print("ciao")
    elif opzione == 3:
        print(vertice_calcolo(a, b, c))
        print(fuoco_calcolo(a, b, c))
    else:
        print("non dovevi premere questo tasto")

main()
