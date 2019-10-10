from functools import reduce
print(reduce(lambda x,y:x+y,range(1,100)))
l1=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l1))
l2=["deeepesh","ranjan"]
print(list(map(lambda x:x+"it",l2)))
