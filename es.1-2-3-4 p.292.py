#esercizio_1 = Crea una classe Atleta per rappresentare le informazioni su un giocatore. La classe deve contenere un attributo booleano chiamato visitaMedica.
#esercizio_2 = Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra dove gioca.
#esercizio_3 = Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visitaMedica uguale a True.
#esercizio_4 = Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.

class atleta:
    def __init__(self ,nome ,altezza ,sport ,anni ,squadra = 0 ,visitaMedica = False):
        self.nome = nome
        self.sport = sport
        self.altezza = altezza
        self.anni = anni
        self.visitaMedica = visitaMedica
        
    def squadra(self ,nome_squadra):
        self.squadra = nome_squadra
        
    def visualizza_dati(self):
        print("Sono un atleta e mi chiamo", self.nome, ", la mia altezza è", self.altezza, "metri , lo sport che pratico è", self.sport,", la mia squadra è", self.squadra, "e ho fatto la visita medica.")
        
    def effettua_visita(self):
        self.visitaMedica = True
        
a1 = atleta("Alessio", 1.90, "basket", 20)
a1.squadra("Roma")
a1.visualizza_dati()
a1.effettua_visita()
