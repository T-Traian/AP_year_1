def prim(x):
    if x<2:
        return 0
    else:
        if x==2:
            return 1
        else:
            if x%2==0:
                return 0
            else:
                for i in range (3,x,2):                 #verify if prime
                    if x%i==0:
                        return 0
    return 1

n=int(input())
if prim(n)==1:
    print (n)
else:
    aux=n
    ok=0
    while ok==0:
        n-=1
        if prim(n)==1:
            cnt1=n
            break
    n=aux
    while ok==0:
        n+=1
        if prim(n)==1:
            cnt2=n
            break
    n=aux
if(n-cnt1<cnt2-n):
    print(cnt1)
else:
    print(cnt2)