class Parent:
    def __init__(self,first,last):
        self.first=first
        self.last=last

class Child(Parent):
    def __init__(self,first,last,id):
        super().__init__(first,last)
        self.id=id

    def disp(self):
        print("first: {} last:{} id:{}".format(self.first,self.last,self.id))

c=Child("deepesh","ranjan",20094713)
c.disp()


class Parent:
    def __init__(self,first,last):
        self.first=first
        self.last=last

class Child(Parent):
    def __init__(self,first,last,id):
        super().__init__(first,last)
        self.id=id

    def __str__(self):
        return "first: {} last:{} id:{}".format(self.first,self.last,self.id)

c=Child("deepesh","ranjan",20094713)
print(c)



class Parent:
    pass

class Child(Parent):
    pass

p=Parent()
c=Child()

print(isinstance(p,Parent))
print(isinstance(c,Parent))
print(isinstance(c,Child))
print(isinstance(p,object))
print(isinstance(c,object))

print(isinstance(p,Child))
