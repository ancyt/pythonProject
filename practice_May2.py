#Leap year

# year=int(input("Enter the year to be checked: "))
#
# if((year%400==0) and (year%100==0)):
#     print("Leap year")
# elif((year%4==0) and (year%100!=0)):
#     print("Leap year")
# else:
#     print("not a leap year")
######################################################################
#Armstrong Number

# def armstrong(num):
#     temp=num
#     order=len(str(temp))
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum=sum+(digit**order)
#         temp=temp//10
#     if sum==num:
#         print("armstrong")
#     else:
#         print("not an armstrong")
#
# n=153
# armstrong(n)

######################################################

#prime number or not

# def isPrime(n):
#     for i in range(2,n):
#         if n%i!=0:
#             return True
#         else:
#             return False
#
# n=int(input("enter a num: "))
# if isPrime(n):
#     print("prime")
# else:
#     print("not prime")

#################################################
#Factorial

# def fact(n):
#     fact_num=1
#     if n ==0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             fact_num=fact_num*i
#         return fact_num
#
# n=int(input("enter a num: "))
# factorial=fact(n)
# print("facorial is:",factorial)

########################################################3
#fibbonacci

# def fibbo(n):
#     n1=0
#     n2=1
#     count=0
#     while count<n:
#         nth=n1
#         n1=n2
#         n2=n1+nth
#         print(nth,end=" ")
#         count+=1
#
# n=10
# fibbo(n)

# def fibbo(n):
#     fibbo_series=[0,1]
#     if n==1:
#         return 0
#     else:
#         while (len(fibbo_series)<n):
#             fibbo_series.append(fibbo_series[-1]+fibbo_series[-2])
#         return fibbo_series
# n=1
# print(fibbo(n))


# def fib_gen(n):
#     n1=0
#     n2=1
#
#     while True:
#         nth=n1
#         n1=n2
#         n2=n1+nth
#         yield nth
#
# n=10
# f=fib_gen(n)
# for i in range(n):
#     print(next(f),end=" ")

#######################################################
#interchange first and last elements in a list

# a=[10,3,67,34,90]
#
# a[0],a[len(a)-1]=a[len(a)-1],a[0]
# print(a)

