#inside the class declearing constructor

class Myclass:
    def m1(self):
        print("instance method")
    def __init__(self):
        print("0-args constructor")

c=Myclass()


class Myclass2:
    def values(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1    #to represent the local var as class var use self keyword
        self.val2=val2
        
    def add(self):
        print(self.val1+self.val2)

    def mult(self):
        print(self.val1*self.val2)

c=Myclass2()
c.values(3,3)
c.add()
c.mult()

print("*********************************")

class Myclass3:
    def m1(self):
        print("m1 method")
        self.m2(10)

    def m2(self,a):
        print("m2 method",a)

c=Myclass3()
c.m1()
print("**************ex-6*******************")

class Emp:
    def __init__(self,eid,ename,esal):
        print(eid)
        print(ename)
        print(esal)
        #conversion of local to class var
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def display(self):
        print(self.eid)
        print(self.ename)
        print(self.esal)

e=Emp(111,"deepesh",2000000)
e.display()

print("**************ex-7*******************")

#printing the ref var
class Myclass7:
    pass
c=Myclass7()
print(c)                #print memory address


class Myclass71:
    def __str__(self):          #it will return str only and if you also not return then also error
        return "deepesh"
c=Myclass71()
print(c)

print("*********************ex-8***************************")

class Emp1:
    def __init__(self,eid,ename,esal):
        #conversion of local to class var
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        return "emp id:{} emp name:{} emp esal{}".format(self.eid,self.ename,self.esal)
e=Emp1(111,"deepesh",2000000)
print(e)


print("************************ex-9******************************")

class Myclass9:
    def __del__(self):
        print("object deleted")

c1=Myclass9()
c2=Myclass9()
del c1
del c2
print("new")


class Myclass91:
    def __del__(self):
        print("object deleted")

c1=Myclass91()
c2=c1
c3=c1                  #executed one time delete function
del c1
del c2
del c3









