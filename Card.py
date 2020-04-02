

class Card(object):

    suit = ""
    rank = ""
    def __init__(self,suit="",rank=""):
        self.suit = suit
        self.rank = rank
    
    def print(self):
        return self.rank + " of "+ self.suit
    

