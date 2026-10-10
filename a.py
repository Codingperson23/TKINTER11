import code


def fun1(n):
    c=0
    c=c+1
    return n*(n+1)/2, c
x,count=fun1(4)


def fun2(n):
    sum=0
    c=0
    for i in range(1,n+1):
        c=c+1
        sum+=i
    return sum, c
x,count=fun2(4)


def fun3(n):
   


def fun3(n):
    sum=0
    c=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
            c=c+1
    return sum, c

x,count=fun3(4)
