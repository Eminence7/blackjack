

import random
from Card import Card

class Deck(object):
    rank = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suit = ["club","spade","heart","diamond"]
    cards = []

    def __init__(self):
        self.initDeck()
    
    def initDeck(self):
        for rank in self.rank:
            for suit in self.suit:
                self.cards.append(Card(suit,rank))
                print("Adding card "+ rank + " of "+ suit + " to deck")

    def printCards(self):
        for card in self.cards:
            print("print card "+ card.rank + " of "+ card.suit + " to deck")

    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
                print("Shuffling card "+ self.cards[i].print() + " to position "+str(i)+ " in deck")

    def draw(self):
        return self.cards.pop()

class Card(object):

    suit = ""
    rank = ""
    def __init__(self,suit="",rank=""):
        self.suit = suit
        self.rank = rank
    
    def print(self):
        return self.rank + " of "+ self.suit


import random

class Hand :
    any_hand =[]

    
    def __init__(self):
        self.total_hand        
        
    def AddCard(self, card) :
        self.any_hand.append(card)

    def Show_Hand ():
        if card1 != card2:
            card1 = random.choice(self.draw())
            card2 = random.choice(self.draw())
            print (card1 and card2)        
            
    def Top_card ():""

    def total_hand():
        for i in self.rank:
            if i== jack or king or queen:
                i=10
            elif i== Ace:
                i =10
                return
            
        card1+card2



from Deck import Deck
def main():
    #creating deck
    deck = Deck()

    #test shuffling
    deck.shuffle()
    print("Shuffling again")
    deck.shuffle()
    deck.printCards()
    print ("Card Total:"+ str(deck.cards.__len__()))

    # test drawing 
    card  = deck.draw();
    print ("Draw card "+ card.print() )
    card  = deck.draw();
    print ("Draw card "+ card.print() )
    card  = deck.draw();
    print ("Draw card "+ card.print() )
    Hand.Show_Hand()
    Hand.total_hand()



if __name__ == '__main__':
    main()  




















    

