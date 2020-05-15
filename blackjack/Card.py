
import wx
from wx.lib.pubsub import pub

class Card(object):

    suit = ""
    rank = ""
    def __init__(self,suit="",rank=""):
        self.suit = suit
        self.rank = rank
    
    def display(self):
        return self.rank + " of "+ self.suit
        # TODO: Show card on screen
        # TODO: Figure out how to "postion" card on screen

