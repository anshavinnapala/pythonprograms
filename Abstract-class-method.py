from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(computer):
    def process(self):
        print("its running")
        
class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
        
com1 = Laptop()

prog1 = Programmer()
prog2.work(com1)
