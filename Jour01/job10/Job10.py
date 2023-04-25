class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km
        self.en_marche = False
        self.reservoir = 50

    def set_marque(self, marque):
        self.marque = marque

    def set_modele(self, modele):
        self.modele = modele

    def set_annee(self, annee):
        self.annee = annee

    def set_km(self, km):
        self.km = km

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.reservoir = reservoir

    def get_marque(self):
        return self.marque

    def get_modele(self):
        return self.modele

    def get_annee(self):
        return self.annee

    def get_km(self):
        return self.km

    def get_en_marche(self):
        return self.en_marche

    def get_reservoir(self):
        return self.reservoir

    def demarrer(self):
        if self.verifier_plein():
            self.en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est trop vide pour démarrer.")

    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête.")

    def verifier_plein(self):
        return self.reservoir > 5

ma_voiture = Voiture("Renault", "Clio", 2015, 50000)


print("Marque : ", ma_voiture.get_marque())
print("Modèle : ", ma_voiture.get_modele())
print("Année : ", ma_voiture.get_annee())
print("Kilométrage : ", ma_voiture.get_km())
print("En marche : ", ma_voiture.get_en_marche())
print("Réservoir : ", ma_voiture.get_reservoir())


ma_voiture.set_marque("Peugeot")
ma_voiture.set_modele("208")
ma_voiture.set_annee(2018)
ma_voiture.set_km(30000)
ma_voiture.set_en_marche(True)
ma_voiture.set_reservoir(40)


print("Marque : ", ma_voiture.get_marque())
print("Modèle : ", ma_voiture.get_modele())
print("Année : ", ma_voiture.get_annee())
print("Kilométrage : ", ma_voiture.get_km())
print("En marche : ", ma_voiture.get_en_marche())
print("Réservoir : ", ma_voiture.get_reservoir())


ma_voiture.demarrer()
ma_voiture.arreter()
