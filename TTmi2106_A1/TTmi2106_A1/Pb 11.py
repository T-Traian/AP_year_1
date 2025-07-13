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
                for i in range (3,x,2):
                    if x%i==0:
                        return 0
    return 1

def nrd(x):
    cnt=0
    while x>0:
        cnt+=1
        x=x//10
    return cnt

n=int(input())
cnt=2
while nrd(cnt)!=n:
    cnt+=1
while nrd(cnt)==n:
    if prim(cnt):
        aux=cnt
        while aux>9:
            aux=aux//10
        if prim(aux):
            print(cnt,' ', end='')
    cnt+=1
