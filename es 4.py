print("area quadrato")
lato_quadrato = int(input("scrivi la lunghezza del lato del quadrato: "))
A_quadrato = lato_quadrato ** 2
print("l'area del quadrato in questione è:", A_quadrato)

print("area rettangolo")
altezza_rettangolo = int(input("scrivi l'altezza del rettangolo: "))
base_rettangolo = int(input("scrivi la base del rettangolo: "))
A_rettangolo = altezza_rettangolo * base_rettangolo
print("l'area del rettangolo in questione è:", A_rettangolo)

print("area tringolo")
altezza_triangolo = int(input("scrivi l'altezza del triangolo: "))
base_triangolo = int(input("scrivi la base del triangolo: "))
A_triangolo = (altezza_triangolo * base_triangolo) / 2
print("l'area del triangolo in questione è:", A_triangolo)

print("area cerchio")
raggio_cerchio = int(input("scrivi la misura del raggio del cerchio: "))
A_cerchio = (raggio_cerchio ** 2) * 3.14
print("l'area del cerchio in questione è:", A_cerchio)
