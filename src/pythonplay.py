# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrew.tuley"
__date__ = "$28-Apr-2015 08:51:28$"

import threading
import time

def worker1(ctrl):
    while ctrl['w1loop'] >0:
        print ("w1:"+str(ctrl['w1loop']))
        time.sleep(1)
        ctrl['w1loop'] -= 1    

def worker2(ctrl):
    while ctrl['w2loop'] >0:
        print ("w2:"+str(ctrl['w2loop']))
        time.sleep(1)
        ctrl['w2loop'] -= 1


if __name__ == "__main__":
    print ("Hello World (or"+__name__+")")
    
    control = {'w1loop':10, 'w2loop':5}
    t1 = threading.Thread(target=worker1, args=(control,))
    t2 = threading.Thread(target=worker2, args=(control,))
    t1.start()
    t2.start()
    
    while control['w1loop'] >0 or control['w2loop'] >0:
        pass
    
    print ('all stop')
    
