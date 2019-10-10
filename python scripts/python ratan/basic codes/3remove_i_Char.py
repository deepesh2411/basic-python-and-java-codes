def remove(str,rem):
    str=str[:rem-1]+str[rem:]
    print(str)


str=input("enter the string")
rem=int(input("enter the place index"))
remove(str,rem)
