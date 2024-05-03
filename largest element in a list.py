def largest_elem(list1):
    max=list1[0]
    for i in range(len(list1)):
        if (list1[i]>max):
            max=list1[i]
    return max


n=int(input("enter the number of elements:"))
list1=[]
print("enter the elements")
for i in range(0,n):
    ele=int(input())
    list1.append(ele)

print(list1)
print(largest_elem(list1))