import time

import Globals


def waiting():
    while not Globals.isProgramEnd:
        Globals.operate=input("\n請輸入要執行的指令\n(cookie/speed/end):")
        print("已接收命令："+Globals.operate)
        time.sleep(1)