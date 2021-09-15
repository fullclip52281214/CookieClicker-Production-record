import win32gui as w32
import time
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline
import keyboard as kb

#視窗擷取程式參考：https://www.itread01.com/article/1426210195.html
def foo(hwnd,mouse):
    if w32.IsWindow(hwnd) and w32.IsWindowEnabled(hwnd) and w32.IsWindowVisible(hwnd):
        titles.add(w32.GetWindowText(hwnd))
    
currentnum=0
def charToInt(c):
    global currentnum
    currentnum=currentnum*10+int(c)
    
    
def extract(lt):
    lt.sort()
    for t in lt:
        if("块饼干" in t):
            for c in range(t.find("块饼干")-1):
                if not t[c] == ',':
                    #print(t[c])
                    charToInt(t[c])


def KBCheck():
    for i in range(200):
        time.sleep(0.05)        
        if(kb.is_pressed("esc")):
            print("ProgramEnd")
            draw(timeline,num)
            #plt.savefig("END.png")

            return 1
        if(kb.is_pressed("s")):
            draw(timeline,num)
            #plt.savefig(str(time.ctime())+'.png')
            
            time.sleep(0.2)   
            return 0
    return 0


def draw(timeline,num):
    plt.plot((timeline),(num))
    plt.title("amount") # title
    plt.ylabel("cookies") # y label
    plt.xlabel("time") # x label 
    plt.grid(True)
    plt.yscale("log")
    plt.savefig("001.png",dpi=230)
    plt.show()

      
        
if __name__=="__main__":
    
    initialTime=time.time()
    
    timeline=[]
    num=[]
    stopFlag=0
    
    while True:    
        titles = set()
        w32.EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        extract(lt)
        timeline.append(int(time.time())-initialTime)
        num.append(int(currentnum))
        
        
        

        
        
        currentnum=0
        
        
        if(KBCheck()):
            break
        
    