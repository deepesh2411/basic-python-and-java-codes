#ex 1 overriding var

#overring child class var executed
class Parent:
    name="deepesh"

class Child(Parent):
    name="ranjan"

c=Child()
print(c.name)

#not overring parent class var executed
class Parent:
    name="deepesh"

class Child(Parent):
    name="ranjan"

c=Child()
print(c.name)


#ex2 overring methods
class Parent:
    def m1(self):
        print("python for testing")

class Child(Parent):
    def m1(self):
        print("python for ML")

c=Child()
c.m1()


class Parent:
    def m1(self):
        print("python for testing")

class Child(Parent):
    pass

c=Child()
c.m1()

#ex3

class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

#common interface
def flying(bird):
    bird.fly()

def swimming(bird):
    bird.swim()
   
#create the object
pa=Parrot()
pen=Penguin()

#passing the object
flying(pa)
flying(pen)
swimming(pa)
swimming(pen)























        
