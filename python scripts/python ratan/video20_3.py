a,b=200,100
class Myclass3:
    a,b=20,10
    def add1(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

    def mul1(self,a,b):
        print(a*b)
        print(self.a*self.b)
        print(globals()['a']*globals()['b'])
    @staticmethod
    def sub1(a,b):
        print(a-b)
        print(Myclass3.a-Myclass3.b)
        print(globals()['a']-globals()['b'])
c=Myclass3()
c.add1(1,2)             #instance method calling
c.mul1(1,2)             #instance method calling
c.sub1(2,1)             #static method calling
print(c.a)              #class var
print(a)                #global var

print("**********************************")
class Myclass2:
    name="deepesh"

c1=Myclass2()
print(c1.name)              #deepesh
c1.name="ranjan"
print(c1.name)              #ranjan
c2=Myclass2()
print(c2.name)              #deepesh
