print("lunghezza parole")
N = int(input("numero delle parole da scrivere: "))
A = []
B = []
n = 1
while True:
    p = input("scrivi parola: ")
    A.append(p)
    B.append(len(p))
    if N == n:
        print("questo è il numero di lettere: ",B)
        break
    n = n + 1
