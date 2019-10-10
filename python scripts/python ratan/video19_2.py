l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=[100,200,300,400,500]

print(list(map(lambda x,y: x+y,l1,l2)))          #[11, 22, 33, 44, 55]
print(list(map(lambda x,y,z: x+y+z,l1,l2,l3)))   #[111, 222, 333, 444, 555]


s="hi deepesh how are you"
words=s.split()
for x in words:
    print(x)

print(words)                             #['hi', 'deepesh', 'how', 'are', 'you']

print(list(map(lambda x:len(x),words)))   #[2, 7, 3, 3, 3]


#reduce

from functools import reduce
print(reduce(lambda x,y:x+y,range(1,100)))   #4950
