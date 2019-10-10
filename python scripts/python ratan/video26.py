print("*****************ex1****************************")
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def disp(self):
        pass
class B(A):
    def disp(self):
        print("abstract method overriding")

b=B()
b.disp()

#a=A()   #TypeError: Can't instantiate abstract class A with abstract methods disp
print("*****************ex2****************************")

class Person(ABC):
    @abstractmethod
    def eat(self):
        pass

class Deepesh(Person):
    def eat(self):
        print("5-idly")

class Ranjan(Person):
    def eat(self):
        print("4-idly")
d=Deepesh()
d.eat()

r=Ranjan()
r.eat()

print("*****************ex3****************************")



class A(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
class Deepesh(A):
    def disp1(self):
        print("god morning")

#r=Deepesh()                #TypeError: Can't instantiate abstract class Deepesh with abstract methods disp2

#second abstract method is not called then error comes we need to implement all the abstract methods


class A(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
    
class Deepesh(A):    #deepesh not able to provide implementation to all abstract method
    def disp1(self):
        print("god morning")
        
class Ranjan(Deepesh):  #but ranjan is able to provide implementation
    def disp2(self):
        print("god AFTERNOON")

#d=Deepesh()          #error
r=Ranjan() 
r.disp1()
r.disp2()

print("*****************ex4****************************")

from abc import ABC,abstractmethod

class A(ABC):
    def __init__(self,values):
        self.values=values
    @abstractmethod
    def disp(self):
        pass
    
class add(A):    
    def disp(self):
        print(10+self.values)
        
class mul(A):  
    def disp(self):
        print(10*self.values)

a=add(20) 
a.disp()
m=mul(5)
m.disp()
