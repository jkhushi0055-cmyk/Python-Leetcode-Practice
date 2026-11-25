# n=int(input("enter your number:"))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"sum of even number is {even}")
# print(f"sum of odd number is {odd}")
# difference=odd-even
# print(f"difference between sum of even and odd number is {difference}")   
# n=int(input("enter your number:"))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"sum of even number from 1 to {n} is {even}") 
# print(f"sum of odd number from 1 to {n} is {odd}")  
# difference=odd-even
# print(f"difference between even and odd number from 1 to {n} is {difference}") 
# n=int(input("enter your number:"))   
# largest=float("-inf")
# smallest=float("inf") 
# for i in range(n):
#     n=int(input("enter your number:"))
#     if n > largest:
#         largest=n
#     if n < smallest:
#             smallest=n
# print(largest)
# print(smallest)
# difference=largest-smallest
# print(f"difference between largest and smallest number is {difference}")    
# n=int(input("enter your number:"))
# smallest= float("inf") 
# largest= float("-inf")
# for i in range(1,n+1):
#     n=int(input("enter your number:"))
#     if n > largest:
#         largest=n
#     if n < smallest :
#         smallest=n
# print(f"smallest number is {smallest}")
# print(f"largest number is {largest}")
# difference=largest-smallest
# print(f"difference between largest and smallest number is{difference}")    
# n=int(input("enter your number:"))
# smallest=float("inf")
# for i in range(n):
#     n=int(input("enter your number:"))
#     if n < smallest:
#         smallest=n
# print(smallest)               
# n=int(input("enter your number:"))
# count=0
# for i in range(n):
#     n=int(input("enter your number:"))
#     if n%10==0:
#         count+=1
# print(count)      
# n=int(input("enter your number:"))
# count=0
# for i in range(1,n+1):
#     if i%10==5:
#         count+=1
# print(count) 
# n=int(input("enter your number:"))
# last=n%10
# while n > 10:
#     digit=n%10
#     break
#     n=n//10
# print(last)
# print(digit)
# if last==digit:
#     print("first and last digit are same ")
# else:
#     print("no,first and last digit are not same")               
# n=int(input("enter your number:"))
# last=n%10 #5
# digit=0
# while n != 0: 
#     digit=n%10   #5 4 3  2  #1
#     n=n//10 #1234 123 12 1


# print(last)
# print(digit)
# if last==digit:
#     print("first and last digit are same")
# else:
#     print("first and last digit are not same")        
# n=int(input("enter your number:"))
# last=n%10
# while n > 10:
#     digit=n%10
#     n=n//10
# if last==digit:
#     print("first and last value are same")
# else:
#     print("firsr and last value are not same ")
# n=int(input("enter your number:"))
# count=0
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         count+=1
# print(count)       
# n=int(input("enter your number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)    
# n=int(input("enter your number:"))
# a=n
# sum=0
# while n > 0:
#     last=n%10
#     fact=1
#     for i in range(1,last+1):
#         fact=fact*i  
        
#     sum=sum+fact    
#     n=n//10
# print(sum)
# if a==sum:
#     print(f"{a} is a strong number")
# else:
#     print(f"{a} is not a strong number")        
# n=int(input("enter your number:"))
# sum=0
# tem=n
# while n > 0:
#     last=n%10
#     fact=1
#     for i in range(1,last+1):
#         fact=fact*i
#     sum=fact+sum
#     n=n//10
# print(sum)
# if tem==sum:
#     print(f"{tem} is a strong number")
# else:
#     print(f"{tem} is not a strong number")  
# n=int(input("enter your number:"))
# sum=0
# temp=n
# while n > 0:
#     fact=1
#     last=n%10
#     for i in range(1,last+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# print(sum)
# if temp==sum:
#     print(f"{temp} is a strong number")
# else:
#     print(f"{temp} is not a strong number")     
# n=int(input("enter your number:"))
# sum=0
# temp=n
# while n > 0:
#     fact=1
#     last=n%10
#     for i in range(1,last+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# print(sum)
# if sum==temp:
#     print(f"{temp} is a strong number")                 
# else:
#     print(f"{temp} is not a strong number")    
# n=int(input("enter your number:"))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)        
# n=int(input("enter your number:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
# n=int(input("enter your number:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
# n=int(input("enter your number:"))
# sum=0
# temp=n
# while n > 0:
#     last=n%10
#     sum=sum+last
#     n=n//10
# if temp%sum==0:
#     print(f"{temp} is a harshad number") 
# else:
#     print(f"{temp} is not a harshad number") 
      

