import move,screenshot,datection
import time
import pyautogui

time.sleep(2)
roop=51
roop2=40
for y in range(roop):
    move.movel(x=5,y=3+12*y)
    for x in range(roop):
        move.move(sx=x,sy=0)

for y in range(roop):
    for i in range(roop):
        datection.ction(sx=i,sy=y)
