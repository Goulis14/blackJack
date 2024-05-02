class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_card(self, card):
        if type(card) == type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)

    def remove_card(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
