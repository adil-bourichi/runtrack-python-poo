class Livre:
    def __init__ (self,titre,auteur,nbr_pages):
        self.__titre=titre
        self.__auteur=auteur
        self.__nbr_pages=nbr_pages
        self.__disponible=True

    def get_titre(self):
        return self.__titre
    def set_titre(self,titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,auteur):
        self.__auteur = auteur

    def get_nbr_pages(self):
        return self.__nbr_pages
    def set_nbr_pages(self,nbr_pages):
        if isinstance(nbr_pages, int) and nbr_pages > 0:
            self.__nbr_pages = nbr_pages
        else:
            print("error")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté ou est déjà disponible.")

livre = Livre("Vie", "adil", 40)
print(livre.verification())  

livre.emprunter() 
print(livre.verification())  

livre.rendre() 
print(livre.verification())  
