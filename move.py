from __future__ import division
import pyautogui
from time import sleep
import screenshot


def move(sx,sy):#1タイル横約211.5縦107.3
    screenshot.screenshot(sx=sx,sy=sy)
    pyautogui.moveTo(1200,511)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(0,511,1)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(113,511)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(0,511,0.5)
    pyautogui.mouseUp(button='left')

#///////////説明////////////////////
#1タイル 縦=80 横=160
#隙間    縦=10 横=30
#よって計算時には半分にして計算する。
#1タイル 縦=40 横=80
#隙間    縦=5 横=15
#足すと
#縦=45 横=95

#/////////////////////ここからロング移動用//////////////////////////////////////
def tap(m):
    ml=list(str(m))
    mp ={"1x":873,"1y":443,"2x":950,"2y":452,"3x":1044,"3y":447,"4x":867,"4y":515,"5x":956,"5y":514,"6x":1041,"6y":508,"7x":867,"7y":576,"8x":952,"8y":579,"9x":1044,"9y":576,"0x":887,"0y":641,"cx":1014,"cy":636}
    for i in range(len(ml)):
        pyautogui.click(mp["{}x".format(ml[i])],mp["{}y".format(ml[i])])
        sleep(0.1)
    pyautogui.click(mp["cx"],mp["cy"])
    sleep(0.1)


def movel(x,y):#xyを指定して移動
    k=150
    pyautogui.click(603,239)
    sleep(0.2)
    pyautogui.click(647,413)#x
    sleep(0.2)
    tap(x)
    pyautogui.click(766,419)#y
    sleep(0.2)
    tap(y)
    pyautogui.click(630,525)
    sleep(0.1)
    pyautogui.click(640,510)
    sleep(0.1)
    pyautogui.click(867,276)

#////////////////////////////ここまで//////////////////////////////////////////

sleep(2)
#movel(20,20)

pos = pyautogui.position()
print(pos)

