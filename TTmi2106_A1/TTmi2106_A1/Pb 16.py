def f(x):
    if x%10<(x//10)%10:
        return 1
    return 0

cnt=0
x=int(input())
if x!=0:
    while x!=0:
        if f(x)==1:
            cnt+=1
        x=int(input())
print (cnt)