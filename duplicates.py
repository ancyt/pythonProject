def find_dup(s):
    dict={}
    duplicates=[]
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for k,v in dict.items():
        print(k,"-",v,",",end=" ")


str1=input("enter a string:")
find_dup(str1)