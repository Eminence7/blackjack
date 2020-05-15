#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import wx


class Start_Home(wx.Frame):

    def __init__(self, *args, **kw):
        super(Start_Home, self).__init__(*args, **kw)

        self.SetSize((500, 400))
        self.SetTitle('Twenny one!! Black Jack Card Game.')
        self.Centre()


      
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
       

        
    def GameWindow(self, e):

        if Game_Quit_btn:
            self.Close(True)
        elif Game_strt_btn:
            return Black_jack_play
        else:
            Game_rules()

    def OnEraseBackground(self, evt):
        """    Add a picture to the background    """
        # yanked from ColourDB.py
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("stock-photo-black-jack-gambling-table.jpg")
        dc.DrawBitmap(bmp, 0, 0)

        

class Black_jack(Start_Home):
    pass

class Game_rules(wx.Frame):
    pass



def main():

    app = wx.App()
    ex = Start_Home(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  
