from random import shuffle
import Main
import Card


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in Main.suits:
            for rank in Main.ranks:
                self.all_cards.append(Card.Card(suit, rank))

    def shuffle_cards(self):
        shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()