class Rectangle:
    def __init__ (self,longueur,largueur):
        self.__longueur=longueur
        self.__largeur=largueur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self,longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self,largeur):
        self.__largeur=largeur

rectangle=Rectangle(10,5)
print(rectangle.get_longueur(),rectangle.get_largeur())
rectangle.set_largeur(20)
rectangle.set_longueur(30)
print(rectangle.get_longueur(),rectangle.get_largeur())
