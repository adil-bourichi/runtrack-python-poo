import random
import json
from pokemon import Pokemon

class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire

    def est_fini(self):
        """Vérifie si l'un des deux Pokémon est mort"""
        return self.joueur.points_de_vie <= 0 or self.adversaire.points_de_vie <= 0

    def get_vainqueur(self):
        """Retourne le nom du vainqueur"""
        if self.joueur.points_de_vie <= 0:
            return self.adversaire.nom
        elif self.adversaire.points_de_vie <= 0:
            return self.joueur.nom
        else:
            return None

    def attaque_reussie(self):
        """Renvoie True si l'attaque réussit, False sinon"""
        return random.randint(0, 1) == 1

    def calcule_degats(self, attaquant, defenseur):
        """Calcule les dégâts infligés par l'attaquant au défenseur"""
        multiplicateur = attaquant.get_multiplicateur_attaque(defenseur.type)
        degats = attaquant.puissance_attaque * multiplicateur - defenseur.defense
        return degats

    def inflige_degats(self, attaquant, defenseur, degats):
        """Inflige les dégâts au défenseur"""
        defenseur.points_de_vie -= max(degats, 0)

    def get_perdant(self):
        """Retourne le nom du Pokémon perdant"""
        if self.joueur.points_de_vie <= 0:
            return self.joueur.nom
        elif self.adversaire.points_de_vie <= 0:
            return self.adversaire.nom
        else:
            return None

    def enregistre_pokemon(self, pokemon):
        """Enregistre le Pokémon rencontré dans le Pokédex"""
        with open("pokedex.json", "r+") as f:
            data = json.load(f)
            if pokemon.nom not in data:
                data[pokemon.nom] = 1
            else:
                data[pokemon.nom] += 1
            f.seek(0)
            json.dump(data, f)

    def lancer_combat(self):
        """Lance le combat entre les deux Pokémon"""
        print("Le combat commence entre {} et {} !".format(self.joueur.nom, self.adversaire.nom))
        tour = 1
        while not self.est_fini():
            print("Tour {}:".format(tour))
            if self.attaque_reussie():
                attaquant = self.joueur
                defenseur = self.adversaire
            else:
                attaquant = self.adversaire
                defenseur = self.joueur
            degats = self.calcule_degats(attaquant, defenseur)
            self.inflige_degats(attaquant, defenseur, degats)
            print("{} attaque {} et inflige {} dégâts !".format(attaquant.nom, defenseur.nom, degats))
            tour += 1
        vainqueur = self.get_vainqueur()
        print("Le vainqueur est {} !".format(vainqueur))
        perdant = self.get_perdant()
        self.enregistre_pokemon(perdant)
