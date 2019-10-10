try:
    num=int(input("enter a number"))
    print(10/num)
    try:
        print("inner try")
        print(10+"ranjan")
    except TypeError as t:
        print("type error")
    else:
        print("inner else block")

except ZeroDivisionError as e:
    print("ZeroDivisionError or ValueError",e)
else:
    print("outer else block")
print("rest of the application")
