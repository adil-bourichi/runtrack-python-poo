class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")
        print(f"Nombre de portes: {self.portes}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule()

ma_voiture = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500, portes=4)

ma_voiture.informationsVehicule()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.roue = roue

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")
        print(f"Nombre de roue = {self.roue}")

ma_moto = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)

ma_moto.informationsVehicule()

