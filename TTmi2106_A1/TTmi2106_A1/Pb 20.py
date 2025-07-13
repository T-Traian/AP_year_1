n=int(input())
p=0
cnt=1
while cnt<=n:
    p+=1
    cnt=pow(2,p)
p-=1
print (p)