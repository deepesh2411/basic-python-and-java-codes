class Myclass1:
    def disp1(self):
        print("instance methood")
        
    @staticmethod
    def disp2(name):
        print("static method",name)

c=Myclass1()
c.disp1()
c.disp2("deepesh")


class Myclass2:
    def disp3(self):
        print("good morning")

    def disp4(self,name):
        print("good evening",name)

c=Myclass2()
c.disp3()
c.disp4("deepesh")


class Myclass3:
    a,b=10,20
    def add(self):     #to represent class variable always use self keyword in instance method
        print(self.a+self.b)

    @staticmethod
    def mul():       #to represent class variable always use classname in static method
        print(Myclass3.a*Myclass3.b)

c=Myclass3()
c.add()               #instance method calling
Myclass3.mul()        #static method calling
