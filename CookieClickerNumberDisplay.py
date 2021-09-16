import win32gui as w32
import time
import matplotlib.pyplot as plt
#PLT seems to have to stay in the main thread?
import threading


print("-----Program Recording-----")   

operate=""
isProgramEnd=False
def waiting():
    global operate
    while not isProgramEnd:
        operate=input("請輸入要執行的指令\n(cookie/speed/end):")
        print("已接收命令："+operate)
        time.sleep(1)

t2 = threading.Thread(target = waiting)
t2.start()


#Window Extractor refer to：https://www.itread01.com/article/1426210195.html
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

isProgramAlive=False
def opCheck():
    global operate,isProgramEnd,isProgramAlive
    time.sleep(0.2)        
    if(operate=="end"):
        print("ProgramEnd")
        isProgramEnd=True
        return 1
    
    if(operate=="cookie"):
        cookies.draw()
        #plt.savefig(str(time.ctime())+'.png')
        operate=""
        time.sleep(0.2)  
        
    elif(operate=="speed"):
        speed.draw()
        #plt.savefig(str(time.ctime())+'.png')
        operate=""
        time.sleep(0.2)   
        
    elif(operate=="alive"):
        isProgramAlive=not isProgramAlive
        operate=""
        
    return 0






def record():
    global cookies,speed,stopFlag,currentnum,titles,previousnum
    while not isProgramEnd:    
        titles=set()        
        w32.EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        extract(lt)
        cookies.time.append(int(time.time()-initialTime))
        cookies.num.append(int(currentnum))
        
        if(previousnum!=currentnum):
            speed.time.append(int(time.time()-initialTime))
            speed.num.append(currentnum-previousnum)
        
     
        if(isProgramAlive):
            print(currentnum)
        
        previousnum=currentnum
        currentnum=0
        time.sleep(1)

t3=threading.Thread(target = record)


class data:
    def __init__(self,time,num):
        self.time=time
        self.num=num
        
    def drawMethod(self,miny,maxy):
        plt.plot((self.time),(self.num))
        plt.axis([0,int(time.time()-initialTime), miny,maxy])
        plt.xlabel("time (sec)") # x label 
        plt.grid(True)
        #plt.savefig("001.png",dpi=230)
        plt.show()
        
    def draw(self):
        if(self==cookies):
            plt.title("Cookie Clicker's Cookies") # title
            plt.ylabel("cookies") # y label
            self.drawMethod(0,float(max(self.num)*1.1))
        elif(self==speed):
            plt.yscale("log")
            plt.title("Cookie Clicker's Production speed(positive only)") # title
            plt.ylabel("speed (log)") # y label
            self.drawMethod(1,float(max(self.num)**1.1))
            
    
        
      
     
if __name__=="__main__":
    
    initialTime=time.time()
    titles = set()
    cookies=data([],[])
    speed=data([],[])
    stopFlag=0
    t3.start()
        
    while True :    
        if(opCheck()):
            break
        
    t2.join()  
    t3.join()