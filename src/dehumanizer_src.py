#!/usr/bin/python
# -*- coding: utf-8 -*-

# V1NT3UM
# contato@vinteum.com
# Dehumanizer - Alien Worlds Minner
# Dist: python -OO -m py_compile <your program.py>

from lib import *
import pyautogui
import time
import sys
import os
import webbrowser

# For Linux
chrome_path = '/usr/bin/google-chrome %s'
url = 'https://play.alienworlds.io/'


# SIZE OF MONITOR
screenWidth, screenHeight = pyautogui.size()
# MOUSE POSITION
currentMouseX, currentMouseY = pyautogui.position()

# MINNER - vinteum.com


def Dehumanizer():

    print("\n" * 130)

    # CONFIDENCE
    CONFLVL = sys.argv[1]
    CLIENT = sys.argv[2]
    ACCOUNT = sys.argv[3]

    BROWSER = './screen/' + CLIENT + '/'

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

    os.system('bash resolution.sh')
    progress(0, 100, 'RESOLUTION')
    time.sleep(1)

    print(':: D3HUM4N1Z3R © GRINDER T21 :: TRILIUM MINNER :: V0.8 :: ' +
          ACCOUNT.upper() + ' :: ' + CLIENT.upper() + ' \r')

    progress(0, 100, 'READY')
    time.sleep(1)

    Login = pyautogui.locateOnScreen(BROWSER + 'login', confidence=CONFLVL)
    progress(0, 100, 'SCANING')
    if (Login != None):
        progress(1, 100, 'LOGIN')
        pyautogui.click(Login)
        time.sleep(_T1)

    LetsStart = pyautogui.locateOnScreen(
        BROWSER + 'letsstart', confidence=CONFLVL)
    if (LetsStart != None):
        progress(0, 100, 'RELOAD')
        pyautogui.hotkey('ctrl', 'f5')
        time.sleep(_T1)

    CPU = pyautogui.locateOnScreen(BROWSER + 'cpu', confidence=0.97)
    if (CPU != None):
        ga('CPU')
        i = _TRYCPUTIMER
        while i > 0:
            progress(0, 100, 'WAITING CPU TIME ' + repr(i))
            i -= 1
            time.sleep(1)

    Close = pyautogui.locateOnScreen(BROWSER + 'close', confidence=0.90)
    if (Close != None):
        progress(0, 100, 'CLOSE!')
        time.sleep(_T1)
        pyautogui.click(Close)

    Error = pyautogui.locateOnScreen(BROWSER + 'error', confidence=0.85)
    if (Error != None):
        progress(0, 100, 'WRaRR!! ERRO!?')
        time.sleep(_T1)
        pyautogui.hotkey('ctrl', 'f5')
        ga('ERROR')

    AhSnap = pyautogui.locateOnScreen(BROWSER + 'ahsnap', confidence=0.90)
    if (AhSnap != None):
        progress(0, 100, 'AH SNAP!')
        time.sleep(_T1)
        pyautogui.click(AhSnap)
        ga('AH SNAP')

    ImHuman = pyautogui.locateOnScreen(BROWSER + 'imhuman', confidence=0.90)
    if (ImHuman != None):
        progress(0, 100, 'Im Human?!! WTF!?')
        time.sleep(_T1)
        pyautogui.click(ImHuman)
        time.sleep(_T1)
        pyautogui.click(ImHuman)
        progress(0, 100, 'Closing...')
        # pyautogui.hotkey('ctrl', 'w')
        time.sleep(_T1)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(_T3)
        progress(0, 100, 'And opening again!')
        webbrowser.get(chrome_path).open(url)
        time.sleep(_T2)
        ga('Im Human')

    # Avocado = pyautogui.locateOnScreen(
    #     BROWSER + 'avocado', confidence=CONFLVL)
    # progress(0, 100, 'SCANING')

    # if(Avocado != None):
    #     pyautogui.click(Avocado)
    #     pyautogui.hotkey('ctrl', 'w')
    #     ga('AVOCADO')
    #     progress(0, 100, 'AVOCADO I LIKE!')
    #     time.sleep(_T1)
    #     pyautogui.press('f5')
    #     return

    Home = pyautogui.locateOnScreen(BROWSER + 'home', confidence=CONFLVL)
    progress(0, 100, 'SCANING')

    if (Home != None):
        progress(0, 100, 'HOME')
        pyautogui.click(Home)
        time.sleep(_T1)
        ga('MINED')
        progress(0, 100, 'SCANING')

    Mine = pyautogui.locateOnScreen(BROWSER + 'mine', confidence=CONFLVL)
    progress(randnum(13, 40), 100, 'SCANING')

    if (Mine != None):
        progress(randnum(13, 40), 100, 'MINEHUB')
        ga('MINEHUB')
        pyautogui.click(Mine)
        time.sleep(_T1)

    # WAIT FOR MINING -----------
    MineButtom = pyautogui.locateOnScreen(
        BROWSER + 'minebuttom', confidence=CONFLVL)
    progress(randnum(40, 50), 100, 'SCANING')

    if (MineButtom != None):
        r = _TWAIT
        i = r
        while i > 1:
            if i > 100:
                sys.stdout.write(':: START IN  :: ' + str(i) +
                                 ' SEC                                             \r')
                sys.stdout.flush()
            else:
                progress(i, 100, 'START IN')

            time.sleep(1)
            i -= 1

        # pyautogui.click(MineButtom)
        pyautogui.click(MineButtom)
        ga('MINING')
        progress(53, 100, 'MINING NOW')

    # MINING -----------
    MiningNow = pyautogui.locateOnScreen(
        BROWSER + 'miningnow', confidence=0.97)
    if(MiningNow != None):

        m = _TMINING
        mt = m
        while mt > 1:

            ClaimNew = pyautogui.locateOnScreen(
                BROWSER + 'claimnew', confidence=CONFLVL)
            if (ClaimNew != None):
                time.sleep(_T1)
                progress(69, 100, 'CLAIM NEW')
                pyautogui.click(ClaimNew)
                time.sleep(_T2)
                return

            if mt > 100:
                sys.stdout.write(':: MINING  :: ' + str(mt) +
                                 ' SEC                                             \r')
                sys.stdout.flush()
            else:
                progress(mt, 100, 'MINING ')

            time.sleep(1)
            mt -= 1

        MiningNow = pyautogui.locateOnScreen(
            BROWSER + 'miningnow', confidence=0.97)
        if(MiningNow != None):
            progress(0, 100, 'BAD MINER... RELOAD...')
            pyautogui.click(MiningNow)
            time.sleep(_T1)
            pyautogui.hotkey('ctrl', 'f5')
            progress(0, 100, 'RELOADING')
            return

    ClaimNew = pyautogui.locateOnScreen(
        BROWSER + 'claimnew', confidence=CONFLVL)
    if (ClaimNew != None):
        progress(69, 100, 'CLAIM NEW')
        pyautogui.click(ClaimNew)
        time.sleep(_T2)

    ClaimCenter = pyautogui.locateOnScreen(
        BROWSER + 'claimcenter', confidence=CONFLVL)
    progress(randnum(51, 60), 100, 'SCANING')

    if (ClaimCenter != None):
        progress(65, 100, 'CLAIM CENTER')
        pyautogui.click(ClaimCenter)
        time.sleep(_T2)

    ClaimButtom = pyautogui.locateOnScreen(
        BROWSER + 'claimbuttom', confidence=CONFLVL)
    progress(70, 100, 'SCANING')

    if (ClaimButtom != None):
        progress(75, 100, 'CLAIM BUTTOM')
        pyautogui.click(ClaimButtom)
        time.sleep(_T2)

    # WAITING FOR CLAIM-----------
    WaitingForClaimA = pyautogui.locateOnScreen(
        BROWSER + 'waitingforclaim_a', confidence=0.97)

    WaitingForClaimB = pyautogui.locateOnScreen(
        BROWSER + 'waitingforclaim_b', confidence=0.97)

    if(WaitingForClaimA != None or WaitingForClaimB != None):

        m = _TCLAIM
        mt = m
        while mt > 1:

            Approve = pyautogui.locateOnScreen(
                BROWSER + 'approve', confidence=CONFLVL)
            if (Approve != None):
                time.sleep(_T1)
                progress(90, 100, 'APPROVE')
                pyautogui.click(Approve)
                time.sleep(_T2)
                return

            if mt > 100:
                sys.stdout.write(':: WAITING FOR CLAIM  :: ' + str(mt) +
                                 ' SEC                                             \r')
                sys.stdout.flush()
            else:
                progress(mt, 100, 'WAITING FOR CLAIM ')

            time.sleep(1)
            mt -= 1

        WaitingForClaimA = pyautogui.locateOnScreen(
            BROWSER + 'waitingforclaim_a', confidence=0.97)
        WaitingForClaimB = pyautogui.locateOnScreen(
            BROWSER + 'waitingforclaim_b', confidence=0.97)
        if(WaitingForClaimA != None or WaitingForClaimB != None):

            progress(0, 100, 'BAD CLAIM... RELOAD...')

            if(WaitingForClaimA != None):
                pyautogui.click(WaitingForClaimA)
                time.sleep(_T1)

            if(WaitingForClaimB != None):
                pyautogui.click(WaitingForClaimB)
                time.sleep(_T1)

            pyautogui.hotkey('ctrl', 'f5')
            progress(0, 100, 'RELOADING')
            time.sleep(_T1)
            return

    Approve = pyautogui.locateOnScreen(BROWSER + 'approve', confidence=CONFLVL)
    progress(90, 100, 'SCANING')

    if (Approve != None):
        progress(90, 100, 'APPROVE')
        pyautogui.click(Approve)
        time.sleep(_T1)
        ga('MINED')
        progress(100, 100, 'SUCCESS')
        time.sleep(_TCLAIM)

        # Waiting = pyautogui.locateOnScreen(
        #     BROWSER + 'waiting', confidence=CONFLVL)
        # if(Waiting != None):
        #     pyautogui.click(Waiting)
        #     time.sleep(_T1)
        #     pyautogui.hotkey('ctrl', 'f5')
        #     progress(0, 100, 'RELOADING')
        #     return

        return

    # ImNotaRobot = pyautogui.locateOnScreen(
    #     BROWSER + 'imnotarobot', confidence=CONFLVL)
    # progress(93, 100, 'SCANING')

    # if (ImNotaRobot != None):
    #     progress(95, 100, 'AM I A ROBOT?')
    #     pyautogui.click(ImNotaRobot)
    #     time.sleep(_T1)

    #     Attempt = 1
    #     Success = pyautogui.locateOnScreen(
    #         BROWSER + 'success', confidence=CONFLVL)
    #     while (Success == None):

    #         Attempt = Attempt + 1

    #         if(Attempt > 6):
    #             time.sleep(_T1)
    #             pyautogui.click(x=screenWidth, y=200)
    #             time.sleep(_T1)
    #             pyautogui.press('f5')
    #             return

    #         Try = pyautogui.locateOnScreen(BROWSER + 'try', confidence=CONFLVL)
    #         if(Try != None):
    #             progress(0, 100, 'TRY?! WRARR BAD CAPCHA!')
    #             pyautogui.click(x=screenWidth, y=200)
    #             pyautogui.press('f5')
    #             ga('TRY CAPCHA')
    #             i = _TRYCPUTIMER
    #             while i > 0:
    #                 progress(0, 100, 'WAITING TRYCAPCHA TIME ' + repr(i))
    #                 i -= 1
    #                 time.sleep(1)

    #             return

    #         Approve = pyautogui.locateOnScreen(
    #             BROWSER + 'approve', confidence=CONFLVL)
    #         if (Approve != None):
    #             progress(99, 100, 'APPROVE')
    #             pyautogui.click(Approve)
    #             time.sleep(_T1)
    #             progress(100, 100, 'SUCCESS')
    #             time.sleep(_T6)

    #             Waiting = pyautogui.locateOnScreen(
    #                 BROWSER + 'waiting', confidence=CONFLVL)
    #             if(Waiting != None):
    #                 pyautogui.click(Waiting)
    #                 time.sleep(_T1)
    #                 pyautogui.press('f5')
    #                 progress(0, 100, 'RELOADING')
    #                 return
    #             return

    #         CapchaHead = pyautogui.locateOnScreen(
    #             BROWSER + 'capchahead', confidence=CONFLVL)
    #         if (CapchaHead != None):
    #             progress(97, 100, 'DECODING')
    #             pyautogui.click(CapchaHead)
    #             time.sleep(_T2)

    #         CapchaEye = pyautogui.locateOnScreen(
    #             BROWSER + 'capchaeye', confidence=CONFLVL)
    #         if (CapchaEye != None):
    #             progress(94, 100, 'ENCODING')
    #             pyautogui.click(CapchaEye)
    #             time.sleep(_T1)

    #         Success = pyautogui.locateOnScreen(
    #             BROWSER + 'success', confidence=CONFLVL)
    #         Approve = pyautogui.locateOnScreen(
    #             BROWSER + 'approve', confidence=CONFLVL)
    #         if (Success != None):
    #             progress(99, 100, 'APPROVE')
    #             pyautogui.click(Approve)
    #             time.sleep(_T1)
    #             ga('MINED')
    #             progress(100, 100, 'SUCCESS')
    #             time.sleep(_T6)

    #             Waiting = pyautogui.locateOnScreen(
    #                 BROWSER + 'waiting', confidence=CONFLVL)
    #             if(Waiting != None):
    #                 pyautogui.click(Waiting)
    #                 time.sleep(_T1)
    #                 pyautogui.press('f5')
    #                 progress(0, 100, 'RELOADING')
    #                 return

    #             return

    # return

# START !


CONFLVL = sys.argv[1]
removefiles()
ga("LOADING")
print("\n" * 130)

print(':: D3HUM4N1Z3R :: ' + larry() + ' \r')
progress(0, 100, 'STARTING...')
time.sleep(1)
progress(0, 100, 'REMOVING TRASH...')
time.sleep(1)
progress(1, 100, 'APPLY CONFIDENCE LEVEL ' + CONFLVL)
time.sleep(1)

while True:
    Dehumanizer()
    # XR()
