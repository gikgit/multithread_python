from types import *
from base.base import Base
import threading

class MultiThreadsP2(Base):
    def __init__(self):
        Base.__init__(self, 2)
        self.threads = []

    def MultiThreadsCompute_all(self, powers):
        if type(powers) is ListType:
            for idx, power in enumerate(powers):
                t = threading.Thread(target=self.compute_all, args=([power], idx))
                self.threads.append(t)
                t.start()
