
import wx
from wx.lib.pubsub import pub

class Card(object):

    suit = ""
    rank = ""
    image = ""
    def __init__(self,suit="",rank=""):
        self.suit = suit
        self.rank = rank
        self.image = self.getCardImage()
    
    def display(self):
        return self.rank + " of "+ self.suit
        # TODO: Show card on screen
        # TODO: Figure out how to "postion" card on screen
    
    def getCardImage(self):

        if self.rank.isnumeric() :
            return "images/"+self.rank+ self.suit[0:1] + ".jpg"
        else: 
            return "images/"+self.rank[0:1]+ self.suit[0:1] + ".jpg"

