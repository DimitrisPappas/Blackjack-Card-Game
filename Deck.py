from Card import *
import random

class Deck:

    def __init__(self):
        self.all_cards = []
        for r in RANKS:
            for s in SUITS:
                self.all_cards.append(Card(s,r))
        # Shuffle deck automatically at initialization
        self.shuffle()

    def shuffle(self):
        # Shuffle deck manually
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        card_names = "DECK:"
        for c in self.all_cards:
            card_names += "\n" + c.__str__()
        return card_names
