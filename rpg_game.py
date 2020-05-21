# Importation des modules
from importlib import import_module


# Initialisation des joueurs
# player1 = Players(input(str("\nJoueur 1: Quel est ton pseudo? ")))
# player2 = Players(input(str("\nJoueur 2: Quel est ton pseudo? ")))

# p1_class = getattr(import_module("core.characters"), player1.classe)
# p1 = p1_class(player1.name)
# print(p1)
# p2_class = getattr(import_module("core.characters"), player2.classe)
# p2 = p2_class(player2.name)
# print(p2)

# Fixed inputs

p1_class = getattr(import_module("core.characters"), "War")
p1 = p1_class("player1", "War")
print(p1)
p2_class = getattr(import_module("core.characters"), "Mage")
p2 = p2_class("player2", "Mage")
print(p2)


def main():

    _round = who_starts(p1, p2)
    _round_number = 0
    game_finished = None

    while game_finished is not True:
        print("____NEW_ROUND____\n")
        _round_number += 1
        for _ in range(2):
            active_player = _round.pop(0)
            passive_player = _round[0]
            print(f"{active_player.name}'s turn")

            active_player_do = active_player.do_damage()
            game_finished = passive_player.take_damage(active_player_do)
            if game_finished is True:
                break            
            _round.append(active_player)

        print(f"Round {_round_number} is ending...\n")
        if game_finished is True:
            print(f"Game is ending...\n")
            break



if __name__ == "__main__":
    from core.helpers import who_starts
    from core.players import Players
    main()