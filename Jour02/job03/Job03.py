class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

rectangle1 = Rectangle(5, 3)

print(rectangle1.get_longueur()) 
print(rectangle1.get_largeur())  

rectangle1.set_longueur(8)
rectangle1.set_largeur(2)

print(rectangle1.surface())      
print(rectangle1.perimetre())    

parallelepipede1 = Parallelepipede(3, 4, 5)

print(parallelepipede1.get_longueur())  
print(parallelepipede1.get_largeur())   

print(parallelepipede1.get_hauteur())   

parallelepipede1.set_hauteur(8)

print(parallelepipede1.volume()) 