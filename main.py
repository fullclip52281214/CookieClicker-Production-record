import time
import threading

from TerminalInputControl import waiting 
from StateExtraction import record
import Globals
Globals.initialize()

print("-----Program Recording-----")   


t2 = threading.Thread(target = waiting)
t2.start()

t3=threading.Thread(target = record)

#Window Extractor refer to：https://www.itread01.com/article/1426210195.html





def opCheck():
    #global operate,isProgramEnd,isProgramAlive
    time.sleep(0.2)        
    if(Globals.operate=="end"):
        print("ProgramEnd")
        Globals.isProgramEnd=True
        return 1
    
    if(Globals.operate=="cookie"):
        Globals.cookies.draw()
        #plt.savefig(str(time.ctime())+'.png')
        Globals.operate=""
        time.sleep(0.2)  
        
    elif(Globals.operate=="speed"):
        Globals.speed.draw()
        #plt.savefig(str(time.ctime())+'.png')
        Globals.operate=""
        time.sleep(0.2)   
        
    elif(Globals.operate=="alive"):
        Globals.isProgramAlive=not Globals.isProgramAlive
        Globals.operate=""
        
    return 0            
        
      
     
if __name__=="__main__":
    
    
    t3.start()
        
    while True :    
        if(opCheck()):
            break
        
    t2.join()  
    t3.join()