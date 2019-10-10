name="deepesh"
def disp():
    #print(name)    error inside the fun if we are using global variable 
    name="ranjan"   #then it is not possible to declare local var with same name
    print(name)
                     #unboundedLocalError
disp()
print(name)


x=10
def disp2():
    #global x    this also we can use if we want to use global var
    x=1       #if we do not use this line then error
    x=x+10     #using of global variable and then using local var with same name
    print(x)
disp2()
