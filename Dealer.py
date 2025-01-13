from Card import *

class Dealer:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        if card.rank == "Ace":
            number_of_Aces_in_hand = 1
            for h in self.hand:
                if h.rank == "Ace":
                    number_of_Aces_in_hand += 1
            ace = card.value    # 11
            if number_of_Aces_in_hand % 2 == 1:
                if self.score() + ace > 21:
                    ace = 1
            else:
                if ace == 1:
                    ace = 11
                else:
                    ace = 1
            card.value = ace
        self.hand.append(card)

    def reset_hand(self):
        self.hand.clear()

    def reveal_hand(self):
        hand_cards = "DEALER:"
        for d in self.hand:
            hand_cards += "\n- " + d.__str__()
        # hand_cards += "\n"
        print(hand_cards)

    def score(self):
        score = 0
        for i in self.hand:
            score += i.value
        return score