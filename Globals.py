import matplotlib.pyplot as plt
#PLT seems to have to stay in the main thread?
import time

def initialize():
    global isProgramEnd,operate,isProgramAlive,initialTime,cookies,speed,data
    isProgramEnd=False
    operate=""
    isProgramAlive=False
    initialTime=time.time()
    

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
                if(len(self.num)>=2):#if self.num not empty
                    plt.yscale("log")
                    plt.title("Cookie Clicker's Production speed(positive only)") # title
                    plt.ylabel("speed (log)") # y label
                    self.drawMethod(1,float(max(self.num)**1.1))
                else:
                    print("Speed has not been extracted. try later")
                
    cookies=data([],[])
    speed=data([],[])