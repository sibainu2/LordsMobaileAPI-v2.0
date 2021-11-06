import pyautogui

from time import sleep
sleep(3)
#このファイルではスクリーンショットを取ります
def screenshot(sx,sy):
    #スクリーンを撮る
    screenshot1 = pyautogui.screenshot(region = (100, 330, 1100, 830))#座標指定してスクリーンショット
    screenshot1.save(r"C:\Users\waon-pc\Desktop\pythonC\discord\lordsmobileAPI\dete\Photo\map_"+str(sx)+"_"+str(sy)+".png")#保存先
#    screenshot2 = pyautogui.screenshot(region = (105, 240, 1080, 778))#1170
#    screenshot2.save(r"C:\Users\waon-pc\Desktop\pythonCドラ\discord\lordsmobileAPI\dete\Photo\map_"+str(i)+"_2.png")#バリア用
  



#screenshot(sx=1,sy=1)
#pyautogui.moveTo(x=106, y=234)
#pos = pyautogui.position()
#print(pos)
