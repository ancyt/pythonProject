#generator_fibbo

def fibbo_gen():
    n1=0
    n2=1
    while True:
        nth=n1
        n1=n2
        n2=n1+nth
        yield nth
f=fibbo_gen()
for i in range(20):
    print(next(f),end=" ")

####################################################

# def fibbo_series(n):
#     fib_series=[0,1]
#     if n in (0,1):
#         return fib_series
#     else:
#         while (len(fib_series)<n):
#             fib_series.append(fib_series[-1]+fib_series[-2])
#     return fib_series
# n=10
# print(fibbo_series(n))

##################################################
# def fibbonacci(n):
#     n1=0
#     n2=1
#     count = 0
#     if(n<0):
#         print("enter positive num")
#     elif (n==0):
#         return n1
#     else:
#         while (count<n):
#            nth=n1
#            n1=n2
#            n2=n1+nth
#            print(nth)
#            count+=1
#
# n=10
# fibbonacci(n)