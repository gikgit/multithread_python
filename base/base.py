from types import *
import threading

lock = threading.Lock()

class Base(object):
    def __init__(self, base):
        self.base = base
        self.res = 0
        self.arr = []

    def compute(self, power):
        if type(power) is IntType:
            if power == 0:
                return 1
            elif power == 1:
                return self.base
            else:
                if power % 2 == 1:
                    self.res = self.compute(power/2)**2*self.base
                    return self.res
                else:
                    self.res = self.compute(power/2)**2
                    return self.res
        else:
            print "parameter should be an integer"

    def compute_all(self, powers, idx=None):
        if type(powers) is ListType:
            if idx == None:
                for power in powers:
                    self.arr.append(self.compute(power))
            else:
                for power in powers:
                    lock.acquire()
                    print "thread "+str(idx)+" is starting", "value="+str(self.compute(power))
                    lock.release()
        else:
            print "parameter should be a list"


    def print_res(self, verbose=False):
        if verbose == True:
            print self.res
            self.res = 0


    def print_all(self, verbose=False):
        if verbose == True:
            print "power of "+str(self.base)+" = "+str(self.arr)
            self.arr = []
