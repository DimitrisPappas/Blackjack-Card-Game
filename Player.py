from Card import *
from itertools import count

class Player:

    ACE = 11

    def __init__(self, balance):
        self.hand = []
        self.balance = balance

    def add_card(self, card):
        if card.rank == "Ace":
            number_of_Aces_in_hand = 1
            for h in self.hand:
                if h.rank == "Ace":
                    number_of_Aces_in_hand += 1
            if number_of_Aces_in_hand % 2 == 1:
                invalidAce = True
                while invalidAce:
                    try:
                        ACE = int(input("Choose Ace's value '1' or '11': \n"))
                    except ValueError:
                        print("Number '1' or '11' is required")
                        continue
                    if ACE == 1 or ACE == 11:
                        invalidAce = False
                    else:
                        print("Number '1' or '11' is required")
            else:
                if ACE == 1:
                    ACE = 11
                else:
                    ACE = 1
            card.value = ACE
        self.hand.append(card)


    def reset_hand(self):
        self.hand.clear()

    def reveal_hand(self):
        hand_cards = "HAND:"
        for h in self.hand:
            hand_cards += "\n- " + h.__str__()
        # hand_cards += "\n"
        print(hand_cards)

    def score(self):
        score = 0
        for i in self.hand:
            score += i.value
        return score

    def add_balance(self, amount):
        self.balance += amount

    def sub_balance(self, amount):
        self.balance -= amount

    def ask(self):
        invalidAsk = True
        while invalidAsk:
            try:
                move = int(input("Hit or Stand?  [Press '1' for hit, '2' for stand]: \n"))
            except ValueError:
                print("Integer number is required")
                continue
            if move == 1:
                # Hit
                return True
            elif move == 2:
                # Stand
                return False
            else:
                print("Invalid input")
                continue

    def bet(self):
        invalidBet = True
        while invalidBet:
            try:
                bet = int(input("Enter bet amount: \n"))
            except ValueError:
                print("Integer number is required")
                continue
            if bet <= 0:
                print("Invalid amount - Bet must be a positive number")
                continue
            if bet > self.balance:
                print("Bet exceeds your balance amount")
                continue
            invalidBet = False
        return bet

    def __str__(self):
        return f"Balance: {self.balance}"