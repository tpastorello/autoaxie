#!/usr/bin/python
# -*- coding: utf-8 -*-

# V1NT3UM
# contato@vinteum.com
# Autoxie - Auto Axie Infinity Player

from lib import *
import pyautogui
import time
import sys
# import os
# import webPATH

# For Linux
# chrome_path = '/usr/bin/google-chrome %s'
# url = 'https://play.alienworlds.io/'


# SIZE OF MONITOR
screenWidth, screenHeight = pyautogui.size()
# MOUSE POSITION
currentMouseX, currentMouseY = pyautogui.position()

# MINNER - vinteum.com


def Autoxie(TEAM, LVLS, TYPE):

    # CHANGE LEVEL RANDOM
    LEVELS = LVLS.split(",")
    LIMIT = len(LEVELS) - 1
    LEVEL = LEVELS[randnum(0, LIMIT)]

    # TURN = 0

    ADVENTURE_TYPE = TYPE

    print("\n" * 130)

    # TIMERS
    _T1 = randnum(1, 3)
    _T2 = randnum(11, 15)
    _T3 = randnum(15, 20)
    _T4 = randnum(17, 33)
    _T6 = randnum(60, 90)
    _TWAIT = randnum(120, 250)

    print(':: AUTOXIE © GRINDER :: SLP MINER :: V0.4 :: ' +
          str(TEAM).upper() + ' IN ' + str(TYPE).upper() + ' '' ::  \r')

    progress(0, 100, 'READY')
    time.sleep(1)
    progress(0, 100, 'SCANING')

    if(ADVENTURE_TYPE == 'adventure'):

        Adventure = LOCATE('adventure')
        if (Adventure != 0):
            progress(5, 100, 'ADVENTURE TIME!')
            pyautogui.click(Adventure)
            time.sleep(_T1)
    else:

        Arena = LOCATE('arena')
        if (Arena != 0):
            progress(5, 100, 'ARENA FIGHT!')
            pyautogui.click(Arena)
            time.sleep(_T1)
            # TURN = 0

    Level = LOCATE('lvl-' + LEVEL)
    if (Level != 0):
        progress(10, 100, 'LEVEL ' + LEVEL)
        pyautogui.click(Level)
        time.sleep(_T2)

    Fifty = LOCATE('5050', 0.999)
    Arrowback = LOCATE('arrowback')
    if (Fifty != 0):
        ADVENTURE_TYPE = 'arena'
        progress(0, 100, 'YOU HAVE FIFTY SLP! LET`S GO TO ARENA')
        time.sleep(_T1)
        pyautogui.click(Arrowback)
        time.sleep(_T2)

        Arena = LOCATE('arena')
        if (Arena != 0):
            progress(5, 100, 'ARENA FIGHT!')
            pyautogui.click(Arena)
            time.sleep(_T2)

    Start = LOCATE('start')
    if (Start != 0):
        progress(20, 100, 'START ')
        pyautogui.click(Start)
        time.sleep(_T2)

    Defeated = LOCATE('defeated')
    if (Defeated != 0):
        progress(0, 100, 'OH NO! DEFEATED !!!!!!')
        pyautogui.click(Defeated)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_TWAIT)

    Victory = LOCATE('victory')
    if (Victory != 0):
        progress(100, 100, 'VICTORY !!!!!!')
        pyautogui.click(Victory)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_TWAIT)

    Draw = LOCATE('draw')
    if (Draw != 0):
        progress(100, 100, 'DRAW !!!!!!')
        pyautogui.click(Draw)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_TWAIT)

    DefeatedB = LOCATE('defeatedb')
    if (DefeatedB != 0):
        progress(0, 100, 'OH NO! DEFEATED !!!!!')
        pyautogui.click(DefeatedB)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_TWAIT)

    VictoryB = LOCATE('victoryb')
    if (VictoryB != 0):
        progress(100, 100, 'VICTORY YEAH !!!!')
        pyautogui.click(VictoryB)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_T1)

    DrawB = LOCATE('drawb')
    if (DrawB != 0):
        progress(100, 100, 'DRAW NOOoO !!!!')
        pyautogui.click(DrawB)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_TWAIT)

    Small = LOCATE('small')
    if (Small != 0):
        progress(100, 100, ' $ GO GO $LP ')
        pyautogui.click(Small)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_T1)

    # SELECT CARDS
    EndTurn = LOCATE('endturn')
    Dismiss = LOCATE('dismiss')
    if (EndTurn != 0 or Dismiss):

        progress(0, 100, 'LET´S PLAY')

        totcards = 12
        i = 1

        # FIRST TURN ONLY FIRST FIVE, ZERO ENERGY CARDS
        # if(TURN == 1):
        #totcards = 5

        while i <= totcards:
            Cards = list(ALLCARDS(i, TEAM))
            TotalCards = len(Cards)

            if(TotalCards > 0):
                progress(i * 8.3, 100, "CARD " +
                         str(i) + " OF " + str(TotalCards))
                CardCount = 0
                while CardCount < TotalCards:
                    pyautogui.click(Cards[CardCount])
                    time.sleep(_T1)
                    pyautogui.doubleClick()
                    CardCount += 1
            # INCREASE
            i += 1

        # pyautogui.moveTo(100, 100)

        # pyautogui.moveTo(100, 100)
        DismissActive = LOCATE('dismiss-active')
        if (DismissActive != 0):
            progress(100, 100, 'DISMISS END')
            pyautogui.click(DismissActive)
            time.sleep(_T1)

        EndTurn = LOCATE('endturn')
        if (EndTurn != 0):
            progress(100, 100, 'END TURN')
            pyautogui.click(EndTurn)
            time.sleep(_T1)
            # TURN INCREESE
            # TURN += 1


# START !
# PARAMETERS
TEAM = sys.argv[1]
TYPE = sys.argv[2]
LEVELS = sys.argv[3]

# REMOVE CACHE
removefiles()
print("\n" * 130)

print('STARTING SLP MINER')
time.sleep(1)

print('TEAM: ' + str(TEAM.upper()) + '\r')
time.sleep(2)

print('TYPE: ' + str(TYPE.upper()) + '\r')
time.sleep(2)

print('LEVELS : ' + str(LEVELS) + '\r')
time.sleep(2)

ga("LOADING AUT0X13")
time.sleep(5)

print('                                                                            \r' + larry() + '  \r')
time.sleep(2)

# AUTOXIE
while True:
    Autoxie(TEAM, LEVELS, TYPE)
