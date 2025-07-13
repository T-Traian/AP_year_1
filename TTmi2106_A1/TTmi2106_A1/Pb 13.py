def f(x):
    cnt=0
    while x>0:
        cnt=cnt*10+x%10
        x=x//10
    return cnt

n=int(input())
cnt=1
aux=f(n)
x=0
while aux>0:
    if cnt%2==1:
        x=x*10+aux%10
    cnt+=1
    aux=aux//10
print(x)