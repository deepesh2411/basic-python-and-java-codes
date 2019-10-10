class Myclass:
    def disp1(self):
        print("good morning")

    def disp2(self,name):
        print("good evening",name)

c=Myclass()
c.disp1()
c.disp2("deepesh")

print("**********************************")
i,j=200,100
class Myclass2:
    a,b=20,10
    def add(self,x,y):
        print(x+y)
        print(self.a+self.b)
        print(i+j)

    def mul(self,x,y):
        print(x*y)
        print(self.a*self.b)
        print(i*j)
    @staticmethod
    def sub(x,y):
        print(x-y)
        print(Myclass2.a-Myclass2.b)
        print(i-j)
c=Myclass2()
c.add(1,2)
c.mul(1,2)
c.sub(2,1)

print("**********************************")
a,b=200,100                                 #global var
class Myclass3:
    a,b=20,10                               #class var
    def add1(self,a,b):                     #local var
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
c.add1(1,2)
c.mul1(1,2)
c.sub1(2,1)
print(c.a)              #class var  20
print(a)                #global var 200 

print("**********************************")
