def p(x):
    a=1
    while x>0:                                  #function to determine the product of the digits
        a=a*(x%10)
        x=x//10
    return a

n=int(input())
k=int(input())
for i in range(pow(10,n-1),pow(10,n)):
    if i==k*p(i):
        print(i,' ',end='')
