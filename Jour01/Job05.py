class Animal:
    def __init__(self,prénom):
        self.age=0
        self.prénom=prénom
    
    def now (self):
        print("L'age de l'animal",self.age,"ans")
    
    def viellir(self):
        print("L'age de l'animal",(self.age+1),"ans")
    
    def nommer(self):
        print("L'animal se nome",self.prénom)

animal=Animal("Luna")

animal.now()
animal.viellir()
animal.nommer()