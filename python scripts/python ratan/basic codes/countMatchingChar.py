def count(str1,str2):
    count=0
    j=0
    for i in str1:
        print("print i: ",i)
        if ((str2.find(i)>= 0) and (j == str1.find(i))):
            count=count+1
            print("count value :",count)
        j+=1
        print("j value :",j)
    print(count)
    
str1=input("enter the first string")
str2=input("enter the second string")
count(str1,str2)
