import Main


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Main.values[rank]
        if self.value == 0:
            self.value = int(input("1 or 11 for ace:"))

    def __str__(self):
        return self.rank + " of  " + self.suit
