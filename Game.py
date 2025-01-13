from Card import *
from Deck import *
from Player import *
from Dealer import *


def replay_game():
    '''
    Ask player if they wish to replay the game
    :return: bool
    '''
    replayOptions = ["Yes", "No", "yes", "no", "y", "n", "Y", "N", "YES", "NO"]
    replayYES = ["Yes", "yes", "y", "Y", "YES"]
    invalidReplayChoice = True
    while invalidReplayChoice:
        replay = input("\nReplay? Yes or No \n")
        if replay in replayOptions:
            invalidReplayChoice = False
    return replay in replayYES


def game():
    '''
    Game Logic of Blackjack card game
    :return: bool (True if balance == 0 / False if balance > 0)
    '''
    # Create and Shuffle Deck
    deck = Deck()
    deck.shuffle()
    # Clear player and dealer hand
    player.reset_hand()
    dealer.reset_hand()
    # Print remaining balance
    print(player)
    # Flags
    game_on = True
    player_won = False
    # Deal first card and ask for bet
    player.add_card(deck.deal())
    player.reveal_hand()
    print(f"Score: {player.score()}")
    bet_amount = player.bet()
    while game_on:
        # Ask for Player's next move
        if player.ask():
            # Hit  -  Player's turn
            player.add_card(deck.deal())
            player.reveal_hand()
            print(f"Score: {player.score()}")
            if player.score() > 21:
                print("BUST")
                game_on = False
                player_won = False
        else:
            # Stand  -  Dealer's turn
            dealer_on = True
            while dealer_on:
                dealer.add_card(deck.deal())
                dealer.reveal_hand()
                print(f"Dealer Score: {dealer.score()}")
                if dealer.score() > 21:
                    print("Dealer BUST")
                    game_on = False
                    player_won = True
                    dealer_on = False
                elif dealer.score() >= player.score():
                    game_on = False
                    player_won = False
                    dealer_on = False
                else:
                    continue
    # Adjust balance
    if player_won:
        player.add_balance(bet_amount)
        print("***  WON  ***")
    else:
        player.sub_balance(bet_amount)
        print("***  LOST  ***")
    # Check if balance reached zero
    zero_balance = False
    if player.balance == 0:
        print("Your balance reached zero")
        print(player)
        zero_balance = True
    return zero_balance



# main
balanceNotPositive = True
while balanceNotPositive:
    try:
        balance = int(input("Enter balance amount: \n"))
    except ValueError:
        print("Integer number is required")
        continue
    if balance <= 0:
        print("Invalid amount - Balance must be a positive number")
        continue
    balanceNotPositive = False
# Create Player
player = Player(balance)
# Create Dealer
dealer = Dealer()
# Flags
replay = True
round = 0
while replay:
    round += 1
    print(f"~~~  Round {round}  ~~~")
    zero_balance = game()
    if zero_balance:
        replay = False
    else:
        replay = replay_game()
print(f"Final Balance: {player.balance}")
print("Thank you for playing!")
