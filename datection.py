import cv2
import pyautogui
from time import sleep
import re
import numpy as np
import math
import json
mapdata={}


Nest={"tiles":"闇の巣窟"}

def ction(sx,sy):
    img_rgb = cv2.imread(r"C:\Users\waon-pc\Desktop\pythonC\discord\lordsmobileAPI\dete\Photo\map_"+str(sx)+"_"+str(sy)+".png")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r"C:\Users\waon-pc\Desktop\pythonC\discord\lordsmobileAPI\dete\Search image\nest.png",0)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    y,x = np.where( res >= threshold)
#    print(x,y)
    print(sx,sy)
    for i in range(len(x)):
        x2=str(math.ceil(x[i]/95+10*sx-1))
        y2=str(math.ceil(y[i]/43-1))
        mapdata["x{}y{}".format(x2,y2)] =Nest
        print(f"座標は{x2},{y2}")


#img_rgb = cv2.imread(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\Photo\map_1_1.png")
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#template = cv2.imread(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\Search image\test_3.png",0)
#res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#threshold = 0.95
#y,x = np.where( res >= threshold)

#1タイル横108縦54
#for i in range(len(x)):
#
#    x=math.ceil(x[i]/108-1)
#    y=math.ceil(y[i]/54-1)
#
#    mapdata["x{}y{}".format(x,y)]["tiles"] ="闇の巣窟"
#
#    print(f"座標は{x},{y}")

#a =json.dumps(mapdata)
#with open(r"C:\Users\waon-pc\Desktop\discord\lordsmobileAPI\dete\map.json","w") as f:
#    f.write(a)
#mapo.close()
