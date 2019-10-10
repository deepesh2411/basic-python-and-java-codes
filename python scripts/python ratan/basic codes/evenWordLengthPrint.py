str="this is deepesh what do you want "
newStr=str.split(" ")
for word in newStr:
    if(len(word)%2==0):
        print(word)
