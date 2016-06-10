from base.base import Base
from multithread.multithread import MultiThreadsP2

instance1 = Base(3)
instance1.compute_all([2,3,4,5])
instance1.print_all(True)

instance2 = MultiThreadsP2()
instance2.MultiThreadsCompute_all([2,3,4,5])
