import Main


class Card:
    def __init__(self, suits, ranks):
        self.suits = Main.suits
        self.ranks = Main.ranks
        self.value = Main.values[ranks]

    def __str__(self):
        return self.ranks + " of " + self.suits
