
import wx
import copy
from wx.lib.pubsub import pub

class UI_Engine(wx.Frame):
    cardBackImage = "images/gray_back.jpg";
    deckPosition = wx.Rect(20,20,20,20)
    dealerPosition = wx.Rect(20,20,20,20)
    playerPosition = wx.Rect(20,20,20,20)
    
    def __init__(self, *args, **kw):
        super(UI_Engine, self).__init__(*args, **kw)
        fullscreenSize = wx.ScreenDC().GetSize();   
        
        self.SetScreenAndCardPosition(fullscreenSize)
       
        self.SetTitle('Twenny one!! Black Jack Card Game.')
        self.Centre()

        self.ButtonPanel = wx.Panel(self,style=wx.SIMPLE_BORDER,size=(400,400),pos = (1000,20))

        self.hitButton = wx.Button(self.ButtonPanel, id=-1, label = "Hit", pos = (47,20), size = (100,26))
        self.stayButton = wx.Button(self.ButtonPanel, id=-1, label = "Stay", pos = (47,48), size = (100,26))
        self.resetButton = wx.Button(self.ButtonPanel, id=-1, label = "Reset", pos = (47,78), size = (100,26))

        self.box = wx.StaticBoxSizer(wx.VERTICAL, self.ButtonPanel, "Box")
        self.box.Add(self.ButtonPanel)
        self.SetSizer(self.box)

      
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        pub.subscribe(self.GameOver,"GameOver")
        pub.subscribe(self.DrawCard,"DrawCard")
        pub.subscribe(self.DisplayHand, "DisplayHand")

    def DisplayHand(self, cards, isDealer):
        images = []
        for card in cards:
            images.append(card.image)
        
        if isDealer: 
            self.DrawStagardImages(self.dealerPosition, images)
        else:
            self.DrawStagardImages(self.playerPosition, images)

    def DrawCard(self, isDealer, cardCount):
        images = []
        for index in range(cardCount):
            images.append(self.cardBackImage)

        if isDealer: 
            self.DrawStagardImages(self.dealerPosition, images)
        else:
            self.DrawStagardImages(self.playerPosition, images)
    
    def DrawStagardImages(self, rect, imageNames, speratory= 30, separtorx = 15):
        for index in range(imageNames.__len__()):
            imageRect = copy.copy(rect)
            imageRect.y += speratory * index
            imageRect.x += separtorx * index
            self.DrawAtPosition(imageNames[index],imageRect)

    def GameOver(self, WhoWin):
        messageBox = wx.MessageDialog(self, "", caption="Game Over",
              style=wx.OK|wx.CENTRE)
        message = ""
        if WhoWin == "Dealer":
            message = "The Dealer wins"
        elif WhoWin == "Player":
            message = "You have won"
        else:
            message = "The game is tied"

        messageBox.SetMessage(message)
        messageBox.ShowModal()
        pub.sendMessage("StartOver")

    def SetScreenAndCardPosition(self, screenSize):
        screenSize.DecBy(100,100)
        self.SetSize(screenSize)
        self.Update()
        screenBox = self.Rect
        
        self.deckPosition = wx.Rect(screenBox.Position,screenBox.Size)
        self.deckPosition.y = int(float(screenBox.Height) * .75) 
        print(self.deckPosition.y)
        print(screenBox.width)
        self.deckPosition.x =  int(float(screenBox.width) * .16)
        self.deckPosition.Height = 100
        self.deckPosition.width = 100

        self.dealerPosition = wx.Rect(screenBox.Position,screenBox.Size)
        self.dealerPosition.y = int(float(screenBox.Height) * .16) 
        print(self.dealerPosition.y)
        print(screenBox.width)
        self.dealerPosition.x =  int(float(screenBox.width) * .5)
        self.dealerPosition.Height = 100
        self.dealerPosition.width = 100

        self.playerPosition = wx.Rect(screenBox.Position,screenBox.Size)
        self.playerPosition.y = int(float(screenBox.Height) * .75) 
        print(self.playerPosition.y)
        print(screenBox.width)
        self.playerPosition.x =  int(float(screenBox.width) * .5)
        self.playerPosition.Height = 100
        self.playerPosition.width = 100
        

    def OnEraseBackground(self, evt):
        """    Add a picture to the background    """
        # yanked from ColourDB.py
        self.initDC()
        bmp = wx.Bitmap("images\stock-photo-black-jack-gambling-table.jpg")
        self.dc.DrawBitmap(bmp, 0, 0)

        deckimages = []
        for index in range(5):
            deckimages.append(self.cardBackImage)

        self.DrawStagardImages(self.deckPosition,deckimages,5,2)

    def initDC(self):
        self.dc = wx.WindowDC(self)
        if not self.dc:
            self.dc = wx.Clientself.dc(self)
            rect = self.GetUpdateRegion().GetBox()
            self.dc.SetClippingRect(rect)
        self.dc.Clear()

    def DrawAtPosition(self,imageName,rect):
        image = wx.BitmapFromImage(wx.ImageFromBitmap(wx.Bitmap(imageName)).Scale(rect.Size.width,rect.Size.height ))
        #card.Scale(wx.Size(200,100))
        self.dc.DrawBitmap(image,rect.Position)