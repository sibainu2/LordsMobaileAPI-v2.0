import move,screenshot,datection
import time
import pyautogui
#このファイルはメインのファイルです。このファイルを実行すると動きます。
time.sleep(2)
roop=51

for y in range(roop):
    move.movel(x=5,y=3+12*y)
    for x in range(roop):
        move.move(sx=x,sy=ｙ)

for y in range(roop):
    for i in range(roop):
        datection.ction(sx=i,sy=y)
