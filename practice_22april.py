# def common_letters(str1,str2):
#     #common_list=[x for x in str1 if x in str2]
#     #return set(common_list)
#     #or
#     lst=set(str1) & set(str2)
#     return lst
#
# string1="shilai"
# string2="himadri"
#
# common=common_letters(string1,string2)
# print(common)
# ########################################################################
# def freq_words(str):
#     list=str.split()
#     print(list)
#     my_dict={}
#
#     for i in list:
#         if i in my_dict:
#             my_dict[i]+=1
#         else:
#             my_dict[i]=1
#     print(my_dict)
#     sorted_dict=sorted(my_dict.items(),key=lambda x: x[1],reverse=True)
#     print(sorted_dict[1])
#
# str="sheena loves eating loves and mango. her sister also loves eating loves and mango."
# freq_words(str)

###################################################################3
#list to dictionary

# def list_to_dic(key,value):
#     result=dict(zip(key,value))
#     print(result)
#
# value=["naina","sheena","jessie"]
# key=[1,2,3]
# list_to_dic(key,value)

########################################################################
# def rev_word(word):
#     temp=""
#     for i in word:
#         temp=i+temp
#     return temp
# def reverse(string):
#     str=string.split()
#     rev_string=""
#     for i in str:
#         reversed=rev_word(i)
#         rev_string=rev_string+reversed+" "
#     print(rev_word(rev_string).strip())
#
# string="ancy is the best"
# reverse(string)

#######################################################
# list1=[4,2,6,8]
# list2=[]
# n=len(list1)
# for i in range(n-1,-1,-1):
#     list2.append(list1[i])
# print(list2)
########################################################

# #generator_fibbo
#
# def fibbo_gen():
#     n1=0
#     n2=1
#     while True:
#         n3=n1
#         n1=n2
#         n2=n1+n3
#         yield n3
# f=fibbo_gen()
# for i in range(20):
#     print(next(f),end=" ")

##################################################
# import re
#
# def isValidPAN(pan):
#     pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
#     return bool(re.match(pattern,pan))
#
# pan="AUVP8847K"
# if isValidPAN(pan):
#     print("valid")
# else:
#     print("invalid")

##################################################
# addition=lambda x,y:x+y
# print(addition(4,5))
#
# twice=lambda a:a*a
# print(twice(4))
################################################3
#merge dictionaries

# dict1={1:"apple",2:"banana"}
# dict2={3:"strawberry",4:"cherry"}
# dict1.update(dict2)
# print(dict1)
# #or
# dict3={**dict1,**dict2}
# print(dict3)
##############################################3
# list1=[23,45,23,67,98]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
n=5
sum=0
for i in range(n):
    for j in range(i+1):
        sum+=1
        print(sum,end=" ")

    print()