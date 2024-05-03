# def rev_string(str):
#     reverse=""
#     for i in str:
#         reverse=i+reverse
#     return reverse
#
#
# string=input("enter the string:")
# reversed_string=rev_string(string)
# print("reversed string is:",reversed_string)

#############################################################

#fibonacci series

# def fibbo_series(n):
#     n1,n2=0,1
#     count=0
#     if n<=0:
#         print("enter positive number!")
#     elif n==1:
#         print(n1)
#     else:
#         while count<n:
#             print(n1,end=" ")
#             nth=n1+n2
#             n1=n2
#             n2=nth
#             count+=1
# n=10
# fibbo_series(n)

# def fibbonacci(n):
#     fibbo_series=[0,1]
#     if(n==0 or n==1):
#         return fibbo_series
#     else:
#         while len(fibbo_series)<n:
#             fibbo_series.append(fibbo_series[-1]+fibbo_series[-2])
#     return fibbo_series
#
# n=10
# print(fibbonacci(n))

########################################################################
#Armstrong

# def armstrong(num):
#     order=len(str(n))
#     sum=0
#
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit**order
#         temp//=10
#     if sum==num:
#         return True
#     else:
#         return False
# n=1634
# if armstrong(n):
#     print(n,"is an armstrong number!")
# else:
#     print(n, "is not an armstrong number!")

###############################################################
#sum of digits

# def sum_of_digits(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum+=digit
#         n//=10
#     return sum
#
# n=153
# print(sum_of_digits(n))

######################################################
#reverse a number

# def reverse_a_number(n):
#     reverse=0
#     while n>0:
#         digit=n%10
#         reverse=(reverse*10)+digit
#         n//=10
#     return reverse
#
# n=154
# print(reverse_a_number(n))

############################################
#reverse a list

# def reverse_list(lst):
#     rev_list=[]
#     n=len(lst)
#     for i in range(n-1,-1,-1):
#         rev_list.append(lst[i])
#     return rev_list
#
# lst=[1,4,2,5,7]
# print(reverse_list(lst))

###################################################
#reverse each word in a string

# def rev(str):
#     temp=""
#     for i in str:
#         temp=i+temp
#     return temp
# def reverse_words(string):
#     lst=string.split(" ")
#     print(lst)
#     revered_str=""
#     for i in lst:
#         reversed=rev(i)
#         revered_str=revered_str+reversed+" "
#     return revered_str
#
# string1="My name is Ancy"
# print(reverse_words(string1))

###########################################################
#count of Capitalized words in a string

# def count_capital(str):
#     count=0
#     str_split=str.split(" ")
#     for i in str_split:
#         if i[0].istitle():
#             count+=1
#             print(i)
#     return count
#
# string="My name is Ancy Thomas. I am a Tester"
# print(count_capital(string))

###################################################################
# find duplicates in a list

# def duplicates_in_a_list(lst):
#     my_dict={}
#     for i in lst:
#         my_dict[i]=my_dict.get(i,0)+1
#     duplicates=[]
#     for k,v in my_dict.items():
#         if v>1:
#             duplicates.append(k)
#     return duplicates
#
# list1=[22,34,33,34,56,78,56,1]
# print(duplicates_in_a_list(list1))

############################################################
#duplicates in a string

# def duplicates_in_a_string(str):
#     my_dict={}
#     string_list=str.split(" ")
#     for i in string_list:
#         my_dict[i]=my_dict.get(i,0)+1
#     print(my_dict)
#
#     duplicates=[]
#     for k,v in my_dict.items():
#         if v>1:
#             duplicates.append(k)
#     return duplicates
#
# string="my name is ancy and ancy"
# print(duplicates_in_a_string(string))

##################################################
import pytest
pytest --help()