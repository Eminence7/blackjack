import random
import wx
from wx.lib.pubsub import pub
from Card import Card

class Hand :
    cards =[]
    value = 0 
    isDealer = False

    def __init__(self, isDealer):
        #TODO: Calculate "Where" this and should be, (dealer section or player section)
        self.isDealer = isDealer
        pass

    def AddCard(self, card):
        self.cards.append(card)
        #TODO: Add gui to show Card

    def show_Card(self, position):
        if len(self.cards) <= position:
            self.cards[position - 1 ].display()

    def Show_Hand (self):
        for card in self.cards:
            card.display()

    def calculate_value(self):
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
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def display(self):
        for card in self.cards: 
            card.display();

    # def Top_card ():``

    # def total_hand():
    #     for i in self.rank:
    #         if i== jack or king or queen:
    #             i=10
    #             else i== Ace:
    #                 i =10
    #          return
            
    #     card1+card2
        

        
        
        

        





