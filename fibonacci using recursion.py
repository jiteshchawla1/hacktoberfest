def fibo(n):
     if n<=1:
          return n
     else:
           return (fibo(n-1)+fibo(n-2))
          
num=int(input("enter the number"))
print("your series is ")
for i in range(num):
     print(fibo(i))
     
