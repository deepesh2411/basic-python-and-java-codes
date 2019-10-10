class InvalidAgeException(Exception):
    def __init__(self,msg):
        self.msg=msg

def status(age):
    if age>20:
        print("eligible for mrg")
    else:
        raise InvalidAgeException("Invalid age for mrg")
x=int(input("enter the age : "))
status(x)
