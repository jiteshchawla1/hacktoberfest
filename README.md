# hacktoberfest
Mainly Python Programs
1.Program to check whether a number is palindrome or not
     num=int(input("Enter a number:"))
     temp=num
     rev=0
     while(num>0):
         dig=num%10
         rev=rev*10+dig
         num=num//10
     if(temp==rev):
         print("The number is palindrome!")
     else:
         print("Not a palindrome!")
2.Program to check  whether a number is prime or not.

num = 11  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 
