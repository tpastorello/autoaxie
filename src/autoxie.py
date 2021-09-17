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

def Autoxie(TEAM, LVLS):

    # CHANGE LEVEL RANDOM
    LEVELS = LVLS.split(",")
    LIMIT = len(LEVELS) - 1
    LEVEL = LEVELS[randnum(0, LIMIT)]

    print("\n" * 130)

    # TIMERS
    _T1 = randnum(1, 3)
    _T2 = randnum(11, 15)
    _T3 = randnum(15, 20)
    _T4 = randnum(17, 33)
    _T6 = randnum(60, 90)
    _TWAIT = randnum(120, 360)

    print(':: AUTOXIE © GRINDER T21 :: AXIE AUTO PLAYER :: V0.1 :: ' +
          TEAM.upper() + ' ::  \r')

    progress(0, 100, 'READY')
    time.sleep(1)
    progress(0, 100, 'SCANING')

    Adventure = LOCATE('adventure')
    if (Adventure != 0):
        progress(5, 100, 'ADVENTURE TIME!')
        pyautogui.click(Adventure)
        time.sleep(_T1)

    Level = LOCATE('lvl-' + LEVEL)
    if (Level != 0):
        progress(10, 100, 'LEVEL ' + LEVEL)
        pyautogui.click(Level)
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
        time.sleep(_T1)
        pyautogui.doubleClick()
        time.sleep(_T1)

    Victory = LOCATE('victory')
    if (Victory != 0):
        progress(100, 100, 'VICTORY !!!!!!')
        pyautogui.click(Victory)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_T1)

    Small = LOCATE('victory')
    if (Small != 0):
        progress(100, 100, ' $$$$$$$$$ ')
        pyautogui.click(Small)
        time.sleep(_T2)
        pyautogui.doubleClick()
        time.sleep(_T1)

    # pyautogui.moveTo(80, 100)

    # SELECT CARDS

    EndTurn = LOCATE('endturn')
    if (EndTurn != 0):

        progress(0, 100, 'LET´S PLAY')

        totcards = 12
        repet = 2
        x = 1

        while x <= repet:
            i = 1
            # print(str(x) + ' x \r')
            # print(str(i) + ' i \r')
            while i <= totcards:
                # print(str(i) + ' i \r')
                Card = CARD(i, TEAM)
                if (Card != 0):
                    progress(0, (i*7), 'CARD ' + str(i))
                    pyautogui.click(Card)
                    time.sleep(_T1)
                    pyautogui.doubleClick()

                i += 1
                time.sleep(1)
                
            x += 1

        # pyautogui.moveTo(100, 100)
        EndTurn = LOCATE('endturn')
        if (EndTurn != 0):
            progress(100, 100, 'END TURN')
            pyautogui.click(EndTurn)
            time.sleep(_T1)
            x = 1

# START !
TEAM = sys.argv[1]
LEVELS = sys.argv[2]

# REMOVE CACHE
removefiles()
print("\n" * 130)

print('STARTING SLP MINER')
time.sleep(1)

print('TEAM: ' + str(TEAM.upper()) + '\r')
time.sleep(3)

print('LEVELS : ' + str(LEVELS) + '\r')
time.sleep(3)

ga("LOADING AUT0X13")
time.sleep(5)

print('                                                                            \r' + larry() + '  \r')
time.sleep(2)

# AUTOXIE
while True:
    Autoxie(TEAM, LEVELS)
