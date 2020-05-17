
from Card import Card
from Hand import Hand
from Deck import Deck
import wx
from wx.lib.pubsub import pub

class Game_Engine:
    player_hand = Hand()
    dealer_hand = Hand(isDealer=True)

    def __init__(self):
        pub.subscribe(self.startGame,"StartOver")
        pub.subscribe(self.HitPlayer,"HitPlayer")
        pub.subscribe(self.StayPlayer,"StayPlayer")

    def play(self):
        playing = True
        
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.player_hand.display()
            
            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.getValue()
                    dealer_hand_value = self.dealer_hand.getValue()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    game_over = True
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def startGame(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(isDealer=True)

        for i in range(2):
            self.player_hand.addCard(self.deck.draw())
            self.dealer_hand.addCard(self.deck.draw())

        self.player_hand.display()        

    def HitPlayer(self):
        self.player_hand.addCard(self.deck.draw())
        self.player_hand.display()
        if self.isBlackJack():
            return
        if self.player_is_over():
            print("You have lost!")
            game_over = True
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Dealer")     
    
    def StayPlayer(self):
        player_hand_value = self.player_hand.getValue()
        dealer_hand_value = self.dealer_hand.getValue()

        if player_hand_value > dealer_hand_value:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Player")     
        elif player_hand_value == dealer_hand_value:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Tie")     
        else:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Dealer")

    def isBlackJack(self):
        player, dealer = self.check_for_blackjack()
        if not player and not dealer:
            return False
        if player and dealer:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Tie")     
        elif player:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Player")     
        else:
            self.dealer_hand.display()
            pub.sendMessage("GameOver",WhoWin="Dealer")
        return True
        

    def player_is_over(self):
        return self.player_hand.getValue() > 21


    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.getValue() == 21:
            player = True
        if self.dealer_hand.getValue() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")
