from core.settings import CLASSES


class Players():
    def __init__(self, name, classe=None):
        # Initialisation d'un joueur
        self.name = name
        self.classe = classe

        # Verification que le joueur prenne une classe qui existe
        while self.classe not in CLASSES: # ["Human", "War", "Mage"]
                print(F"Votre classe est {self.classe}")
                self.classe = input(str("Quelle est ta classe? ")).lower().capitalize()
