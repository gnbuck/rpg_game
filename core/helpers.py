from random import randint

def who_starts(p1, p2):
    coin_1 = (randint(0,100))
    coin_2 = coin_1
    while coin_2 == coin_1:
        coin_2 = (randint(0,100))
    if coin_1 > coin_2:
        return list([p1, p2])
    return list([p2, p1])
