l1=[10,4,5,2,20]
l2=['ratan','anu','durga','ratan']
#using normal method
def m1(x):
    if x%2==0:
        return True
    else:
        return False

print(list(filter(m1,l1)))

#using lambda expression
print(list(filter(lambda x:x%2==0,l1)))
print(tuple(filter(lambda x:x%2==0,l1)))


print(list(filter(lambda x:x=="ratan",l2)))

l3=[4,8,10,24]
def m2(x):
    return x*5

print(list(map(m2,l3)))              #using normal method

print(list(map(lambda x:x*5,l3)))    #using lambda expression
print(list(filter(lambda x:(x+'deep'),l2)))
