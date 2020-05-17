
import wx
from wx.lib.pubsub import pub

class UI_Engine(wx.Frame):
    
    deckPosition = wx.Rect(20,20,20,20)
    dealerPosition = wx.Rect(20,20,20,20)
    playerPosition = wx.Rect(20,20,20,20)
    dc = ""
    def __init__(self, *args, **kw):
        super(UI_Engine, self).__init__(*args, **kw)
        fullscreenSize = wx.ScreenDC().GetSize();   
        
        self.SetScreenAndCardPosition(fullscreenSize)
       

        self.SetTitle('Twenny one!! Black Jack Card Game.')
        self.Centre()


      
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
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
        self.dc = evt.GetDC()
        if not self.dc:
            self.dc = wx.Clientself.dc(self)
            rect = self.GetUpdateRegion().GetBox()
            self.dc.SetClippingRect(rect)
        self.dc.Clear()
        bmp = wx.Bitmap("images\stock-photo-black-jack-gambling-table.jpg")
        self.dc.DrawBitmap(bmp, 0, 0)

        self.DrawAtPosition("images/gray_back.jpg",self.deckPosition)
        self.DrawAtPosition("images/gray_back.jpg",self.dealerPosition)
        self.DrawAtPosition("images/gray_back.jpg",self.playerPosition)  

    def DrawAtPosition(self,imageName,rect):
        image = wx.BitmapFromImage(wx.ImageFromBitmap(wx.Bitmap(imageName)).Scale(rect.Size.width,rect.Size.height ))
        #card.Scale(wx.Size(200,100))
        self.dc.DrawBitmap(image,rect.Position)