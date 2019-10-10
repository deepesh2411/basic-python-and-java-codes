print("********************ex1***************")
class Parent():
    def m1(self):
        print("parent class")

class Child(Parent):
    def m2(self):
        print("child class")

p=Parent()
p.m1()

c=Child()
c.m1()
c.m2()
print("********************ex2***************")

class Parent():
    def m1(self):
        print("parent class")

class Child(Parent):
    def m2(self):
        super().m1()
        print("child class")

c=Child()
c.m2()
print("********************ex3***************")

class Parent():
    a,b=10,20

class Child(Parent):
    x,y=100,200
    def add(self,i,j):
        print(i+j)
        print(self.x+self.y)
        print(self.a+self.b)   #first check in child class if not then parent class

c=Child()
c.add(1000,2000)

print("********************ex4***************")

a,b=1,2
class Parent():
    a,b=10,20

class Child(Parent):
    a,b=100,200
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)   #first check in child class if not then parent class
        print(globals()['a']+globals()['b'])
c=Child()
c.add(1000,2000)

print("********************ex5***************")

class Parent:
    def __init__(self):
        print("parent class const")

class Child(Parent):
    pass

c=Child()      #first check the const in child class then parent class executed

print("********************ex6***************")

class Parent:
    def __init__(self):
        print("parent class const")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("child class const")

c=Child() 















