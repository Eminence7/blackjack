#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import wx


class Start_Home(wx.Frame):

    def __init__(self, *args, **kw):
        super(Start_Home, self).__init__(*args, **kw)

        self.SetSize((350, 250))
        self.SetTitle('Twenny one!! Black Jack Card Game.')
        self.Centre()


        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        bmp = wx.Bitmap("homescreen.jpg")
        pnl.Add(bmp, flag = wx.EXPAND,)
           
        Game_strt_btn = wx.Button(pnl, label='Game Start', pos=(120, 100))
        Game_strt_btn.Bind(wx.EVT_BUTTON, self.GameWindow(self))

        Game_Quit_btn = wx.Button(pnl, label='Quit', pos=(120, 130))
        Game_strt_btn.Bind(wx.EVT_BUTTON, self.GameWindow(self))

        Game_rules_btn = wx.Button(pnl, label='Game Help', pos=(120, 160))
        Game_strt_btn.Bind(wx.EVT_BUTTON, self.GameWindow(self))

        

          

    def GameWindow(self, e):

        if Game_Quit_btn:
            self.Close(True)
        elif Game_strt_btn:
            return Black_jack_play
        else:
            Game_rules()


             


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
