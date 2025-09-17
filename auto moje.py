class kamion:
    nosnost = 3000
    nalozene = 0
    def nakladka(self, hmotnost):
        if self.nosnost >= self.nalozene + hmotnost:
            self.nalozene += hmotnost
    def vykladka(self, hmotnost):
        if self.nalozene >= hmotnost:
            self.nalozene -= hmotnost
    def zostatok(self):
        print(f"The truck is loaded with {self.nalozene}kg")

kamion = kamion()
kamion.nakladka(10000)
kamion.nakladka(500)
kamion.vykladka(300)
kamion.vykladka(1000)
kamion.zostatok()
