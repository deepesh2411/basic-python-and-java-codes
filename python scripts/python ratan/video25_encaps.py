class A:
    num1,num2=100,200
class B:
    def add(self):
        a=A()                  #creating object in every methods prob
        print(a.num1+a.num2)

    def mul(self):
        a=A()
        print(a.num1*a.num2)

b=B()
b.add()
b.mul()


class A:
    num1,num2=10,20
class B:
    a=A()                               #class level var
    def add(self):
        print(self.a.num1+self.a.num2)  #by using self keyword    

    def mul(self):
        print(self.a.num1*self.a.num2)

b=B()
b.add()
b.mul()
