def reverse(num):
    rev_num=0
    while num>0:
        digit=num%10
        rev_num=(rev_num*10)+digit
        num=num//10
    return rev_num

num=int(input("Enter a number:"))
rev_num=reverse(num)
print("reversed num is :",rev_num)