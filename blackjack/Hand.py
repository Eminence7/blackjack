import random
import wx
from wx.lib.pubsub import pub
from Card import Card

class Hand :

    def __init__(self, isDealer=False):
        self.cards =[]
        self.value = 0 
        self.isDealer = False

        #TODO: Calculate "Where" this and should be, (dealer section or player section)
        self.isDealer = isDealer

    def addCard(self, card):
        self.cards.append(card)
        pub.sendMessage("DrawCard",isDealer=self.isDealer, cardCount=self.cards.__len__())
        #TODO: Add gui to show Card Back

    def showCard(self, position):
        if len(self.cards) <= position:
            self.cards[position - 1 ].display()

    def calculateValue(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank.isnumeric():
                self.value += int(card.rank)
            else:
                if card.rank == "Ace":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10 
    
    def getValue(self):
        self.calculateValue()
        return self.value
    
    def display(self):
        pub.sendMessage("DisplayHand",cards = self.cards, isDealer = self.isDealer)
        

    # def Top_card ():``

    # def total_hand():
    #     for i in self.rank:
    #         if i== jack or king or queen:
    #             i=10
    #             else i== Ace:
    #                 i =10
    #          return
            
    #     card1+card2
        

        
        
        

        





