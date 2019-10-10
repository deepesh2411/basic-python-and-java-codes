#else block is executed always when there is no exception in try block

try:
    x=int(input("enter a number"))
    print(10/x)
    print("ranjan")
except ZeroDivisionError as e:
    print("rest of the app")

except:                             #default except block
    print("python for programming")
else:
    print("else block")
#default except block : except without exception
    
#default except must be last

#input----0,5,ratan try with ths values to know the things
