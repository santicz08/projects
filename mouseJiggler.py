import pyautogui as pyg
import random
from time import sleep
import keyboard

cCords = pyg.position()
afk = 0
keys = "q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m"

while True:
    if pyg.position() == cCords:
        afk += 1
    else:
        afk = 0
        cCords = pyg.position()
    if afk == 5:
        x = random.randint(1000, 1500)
        y = random.randint(1, 1000)
        pyg.moveTo(x, y, 0,2)
        cCords = pyg.position()

    sleep(2)
