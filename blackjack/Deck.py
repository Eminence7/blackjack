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
        if len(self.cards) > 1:
            return self.cards.pop()