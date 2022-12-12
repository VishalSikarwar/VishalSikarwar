h1="hello"
h2="hello"
print(id(h1))
print(id(h2))
a=str("Lovely professional university")
print(a [-1:-5:-2])
print(a[: :-1])
str1="Hello Python"
str2="I love"
d=str2[0:6]
e=str1[5:12]
f=d+e
print(f)
#comparison of string
S1="ABC"
S2="abc"
print(S1==S2)
print(S1>S2)
print(S1<S2)
#format method
a='{}plus{}equal{}'.format(4,5,'9')
print(a)
x="python programming"
print(x.swapcase())
x="dqsfsfef"
a="aeiouAEIOU"
for i in x:
    if i in a:
        print(i)
#list
#l1=["hi","9","boom"]
#l2=["sq","4","pen"]
#print(l1+l2)
#p#rint(3*l1)
#list comprehension
#=[1,2,3,4,5,6,7,8,9,]
#l1=[]
#l2=[]
#for i in range(l):
    #if i%2==0:
        #l1.append()
    #else:
        #l2.append()
#print("list",l1)
#print("even",l2)

list1=["aman","ji","hai"]       
list1.insert(2,"naman")
print(list1)
list1.insert(3,"kine")
print(list1)
list1.pop(3)
print(list1)
list1.remove("aman")
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
s=("welcome to python")
print(s.split())

  


    
