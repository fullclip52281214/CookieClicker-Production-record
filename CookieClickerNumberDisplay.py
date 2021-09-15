import win32gui as w32
import time
import matplotlib.pyplot as plt
#PLT seems to have to stay in the main thread?
import threading


operate=""
isProgramEnd=False
def waiting():
    global operate
    while not isProgramEnd:
        operate=input("請輸入要執行的指令\n(show/end):")
        print("命令是"+operate)
        time.sleep(1)

t2 = threading.Thread(target = waiting)
t2.start()


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
            if("e+" in t):
                global currentnum
                currentnum=int(float(t[0:t.find("块饼干")-1]))#科學記號轉INT
            else:            
                for c in range(t.find("块饼干")-1):
                    if not t[c] == ',':
                        #print(t[c])
                        charToInt(t[c])


def opCheck():
    global operate,isProgramEnd
    for i in range(20):
        time.sleep(0.05)        
        if(operate=="end"):
            print("ProgramEnd")
            isProgramEnd=True
            return 1
        
        if(operate=="show"):
            draw(timeline,num)
            #plt.savefig(str(time.ctime())+'.png')
            operate=""
            time.sleep(0.2)   
            return 0
    return 0


def draw(timeline,num):
    plt.plot((timeline),(num))
    plt.axis([0,int(time.time()-initialTime), 0,float(1.1*max(num))])
    plt.title("amount") # title
    plt.ylabel("cookies") # y label
    plt.xlabel("time") # x label 
    plt.grid(True)
    #plt.yscale("log")
    #plt.savefig("001.png",dpi=230)
    plt.show()



def record():
    global num,timeline,stopFlag,currentnum,titles
    while not isProgramEnd:    
        titles=set()        
        w32.EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        extract(lt)
        timeline.append(int(time.time()-initialTime))
        num.append(int(currentnum))
        #print(currentnum)
        currentnum=0
        time.sleep(1)

t3=threading.Thread(target = record)

      
        
if __name__=="__main__":
    
    initialTime=time.time()
    titles = set()
    timeline=[]
    num=[]
    stopFlag=0
    t3.start()
        
    while True :    
        if(opCheck()):
            break
        
    t2.join()  
    t3.join()