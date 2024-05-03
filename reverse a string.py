def reverse(string):
    temp=""
    for i in string:
        temp=i+temp
    print(temp)

str="hello"
reverse(str)