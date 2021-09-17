import win32gui as w32
import time

import Globals
#Globals.initialize()





titles = set()

def foo(hwnd,mouse):
    if w32.IsWindow(hwnd) and w32.IsWindowEnabled(hwnd) and w32.IsWindowVisible(hwnd):
        titles.add(w32.GetWindowText(hwnd))
    
currentnum=0
previousnum=0
def charToInt(c):
    global currentnum
    currentnum=currentnum*10+int(c)
    
    
def extract(lt):
    lt.sort()
    for t in lt:
        if("块饼干" in t):
            if("飞升" in t):#用法待確認
                break
            if("e+" in t):
                global currentnum
                currentnum=int(float(t[0:t.find("块饼干")-1]))
            else:            
                for c in range(t.find("块饼干")-1):
                    if t[c]=='.':
                        break
                    elif not t[c] == ',':
                        #print(t[c])
                        charToInt(t[c])








def record():
    global currentnum,titles,previousnum
    while not Globals.isProgramEnd:    
        titles=set()        
        w32.EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        extract(lt)
        Globals.cookies.time.append(int(time.time()-Globals.initialTime))
        Globals.cookies.num.append(int(currentnum))
        
        if(previousnum!=currentnum and currentnum>previousnum and previousnum!=0):#it's a good idea?
            Globals.speed.time.append(int(time.time()-Globals.initialTime))
            if(len(Globals.speed.time)>=2):
                Globals.speed.num.append((currentnum-previousnum)/(Globals.speed.time[-1]-Globals.speed.time[-2]))
            else:
                Globals.speed.num.append(1)
     
        if(Globals.isProgramAlive):
            print(currentnum)
        
        previousnum=currentnum
        currentnum=0
        time.sleep(1)





 