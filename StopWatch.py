# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:59:21 2018

@author: Abd El-Rahman
"""
import time

Start=0.0
Stop=0.0
class StopWatch(object):
    def __init__(self):
        self.timestamp1=time.time()
    def Start(self):
        self.timestamp1=time.time()
    def Reset(self):
        self.timestamp1=time.time()
    def Stop(self):
        return (time.time()-self.timestamp1)*1000
    def Print(self):
        print(str((time.time()-self.timestamp1)*1000)+' milliseconds')

# Reset and Print Method
    def RP(self):
        print(str((time.time()-self.timestamp1)*1000)+' milliseconds')
        self.timestamp1=time.time()

