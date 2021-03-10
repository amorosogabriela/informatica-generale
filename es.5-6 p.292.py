#esercizio_5 = Elenca propietà e metodi della classe prodotto.
#esercizio_6 = Definisci il metodo assegna_prezzo della classe prodotto.

class prodotto:
    def __init__(self, nome,  numero, provenienza, prezzo):
        self.nome = nome
        self.numero = numero
        self.prezzo = prezzo

    def assegna_prezzo(self):
        self.prezzo = self.prezzo * self.numero

    def info(self):
        print("il prodotto", self.nome, "ha un prezzo di", self.prezzo, "euro.")

p1 = prodotto("tavolo", 2,"Italia", 220)
p1.assegna_prezzo()
p1.info()
