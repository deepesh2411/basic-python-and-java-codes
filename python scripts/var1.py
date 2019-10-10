a,b=10,20                                  #global variable
def add(a,b):                              #local variable
    print(a+b)
    print(globals()['a']+globals()['b'])   

def mul(a,b):
    print(a*b)
    print(globals()['a']*globals()['b'])

def mul1(a,b):
    print(a*b)
    print(a*b) #local variable is prefered if local and global variable having same name

add(3,3)
mul(4,4)
mul1(4,4)
print(a,b)
