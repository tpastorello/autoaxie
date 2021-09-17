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


def Autoxie():

    print("\n" * 130)

    # CONFIDENCE
    CONFLVL = sys.argv[1]
    ACCOUNT = sys.argv[2]

    #PATH = './screen/'

    # TIMERS
    _T1 = randnum(5, 10)
    _T2 = randnum(11, 15)
    _T3 = randnum(15, 20)
    _T4 = randnum(17, 33)
    _T6 = randnum(60, 90)
    _TWAIT = randnum(120, 360)
    _TMINING = randnum(240, 360)
    _TCLAIM = randnum(60, 100)
    _TRYCPUTIMER = 3600

    # os.system('bash resolution.sh')
    # progress(0, 100, 'RESOLUTION')
    # time.sleep(1)

    print(':: AUTOXIE © GRINDER T21 :: AXIE AUTO PLAYER :: V0.1 :: ' +
          ACCOUNT.upper() + ' ::  \r')

    progress(0, 100, 'READY')
    time.sleep(1)    
    progress(0, 100, 'SCANING')

    Adventure = pyautogui.locateOnScreen(PATH('adventure'), confidence=CONFLVL)
    if (Adventure != None):
        progress(1, 100, 'ADVENTURE')
        pyautogui.click(Adventure)        
        pyautogui.doubleClick()
        time.sleep(_T1)

#    LetsStart = pyautogui.locateOnScreen(
#        PATH + 'letsstart', confidence=CONFLVL)
#    if (LetsStart != None):
#        progress(0, 100, 'RELOAD')
#        pyautogui.hotkey('ctrl', 'f5')
#        time.sleep(_T1)


    # WAIT FOR MINING -----------
    # MineButtom = pyautogui.locateOnScreen(
    #     PATH + 'minebuttom', confidence=CONFLVL)
    # progress(randnum(40, 50), 100, 'SCANING')

    # if (MineButtom != None):
    #     r = _TWAIT
    #     i = r
    #     while i > 1:
    #         if i > 100:
    #             sys.stdout.write(':: START IN  :: ' + str(i) +
    #                              ' SEC                                             \r')
    #             sys.stdout.flush()
    #         else:
    #             progress(i, 100, 'START IN')

    #         time.sleep(1)
    #         i -= 1


# START !


CONFLVL = sys.argv[1]
# removefiles()
ga("LOADING")
print("\n" * 130)

print(':: AUT0X13 :: ' + larry() + ' \r')
progress(0, 100, 'STARTING...')
time.sleep(1)
progress(0, 100, 'REMOVING TRASH...')
time.sleep(1)
progress(1, 100, 'APPLY CONFIDENCE LEVEL ' + CONFLVL)
time.sleep(1)

while True:
    Autoxie()
    # XR()
