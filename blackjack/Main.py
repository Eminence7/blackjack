#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
from wx.lib.pubsub import pub

from Card import Card
from Hand import Hand
from Deck import Deck
from UI_Engine import UI_Engine
from Game_Engine import Game_Engine


def main():
    gameEngine = Game_Engine()
    
    app = wx.App()
    ex = UI_Engine(None)
    ex.Show()
    gameEngine.startGame()
    app.MainLoop()


if __name__ == '__main__':
    main()  
