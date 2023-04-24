class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def show_info(self):
        print("Le nombre 1 est",self.nombre1)
        print("Le nombre 2 est",self.nombre2)

operation=Operation(12,3)
operation.show_info()