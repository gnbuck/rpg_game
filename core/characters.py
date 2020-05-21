from random import randint

from core.players import Players

class Human(Players):

    def __init__(self, name, classe):
        super().__init__(name, classe)
        self.hp = 100
        self.strengh = 15
        self.defense = 15
        self.speed = 50


    def __str__(self, super_desc=None, super_stats=None):
        desc = f"Je m'appelle {self.name} et je suis un "
        if super_desc:
            desc += super_desc
        else:
            desc += f"simple {self.classe}.\n"
        stats = f"Mes stats sont : \nhp = {self.hp}\nstrengh = {self.strengh}\ndefense = {self.defense}\nspeed = {self.speed}\n"
        if super_stats:
            stats += super_stats
        desc = desc + stats
        return desc

    def do_damage(self, damage=None):
        print(f"{self.name} prepare un coup a {damage}")
        return damage

    def take_damage(self, input_damage):
        global game_finished
        evade = randint(0, 100)
        if evade <= self.defense:
            print(f"{self.name} a esquive le coup")
            return
        self.hp -= input_damage
        if self.hp <= 0:
            print(f"{self.name} est DCD, il n'etait pas si fort que ca...")
            game_finished = True
            return game_finished
        print(f"{self.name} takes {input_damage} damages and now have {self.hp} HP.")
        return


class War(Human):

    def __init__(self, name, classe):
        super().__init__(name, classe)
        self.hp = randint(90, 120)
        self.armor = 20
        self.speed = 40

    def __str__(self):
        desc =  f"un furieux {self.classe}.\n"
        stats = f"armor = {self.armor}\n"
        return super().__str__(desc, stats)

    def do_damage(self):
        return super().do_damage(self.strengh)

    def take_damage(self, input_damage):
        reduced_damage = input_damage * (1 - self.armor / 100)
        return super().take_damage(reduced_damage)


class Mage(Human):

    def __init__(self, name, classe):
        super().__init__(name, classe)
        self.hp = randint(60, 85)
        self.magic = 30

    def __str__(self):
        desc = f"un puissant {self.classe}.\n"
        stats = f"magic = {self.magic}\n"
        return super().__str__(desc, stats)

    def do_damage(self):
        critic = randint(0, 100)
        if critic <= self.magic:
            print("Critical hit!")
            return super().do_damage(self.strengh * 1.5)
        return super().do_damage(self.strengh)

    def take_damage(self, input_damage):
        return super().take_damage(input_damage)
