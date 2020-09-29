list1=[]
n=int(input("enter the number"))
i=0
while i<n:
     x=int(input("enter the element of list"))
     list1.append(x)
     i=i+1
print(list1)
m=max(list1)
n=min(list1)
mean=sum(list1)/len(list1)
print(m)
print(n)
print(mean)
