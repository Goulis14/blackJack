from blackjack import Player

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9
          , "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 0}


#game logic

player = Player.Player(input("What is your name? "))
dealer = Player.Player("Dealer")

new_deck = Deck.Deck()
new_deck.shuffle_cards()

gameOn = True

for i in range(2):
    player.add_card(new_deck.deal_card())
    print(f"player has: {player.all_cards}")
    dealer.add_card(new_deck.deal_card())
print(f"dealer has : {dealer.all_cards}")
# roundNum = 0
# while gameOn:
#     roundNum += 1
#     print(f"---- Round {roundNum} ----")
#
#
