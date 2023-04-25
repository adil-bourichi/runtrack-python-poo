class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print("Age de la personne :", self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, age):
        self.age = age
        
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()
print("Age de l'élève par défaut :", eleve1.age)