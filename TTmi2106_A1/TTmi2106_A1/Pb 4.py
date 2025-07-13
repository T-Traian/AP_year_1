#problem 4
n=int(input())
cnt=0
a0=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
while n>0:
    if n%10==0:
        a0+=1
    if n%10==1:
        a1+=1
    if n%10==2:
        a2+=1
    if n%10==3:
        a3+=1
    if n%10==4:
        a4+=1
    if n%10==5:
        a5+=1
    if n%10==6:
        a6+=1
    if n%10==7:
        a7+=1
    if n%10==8:
        a8+=1
    if n%10==9:
        a9+=1
    n=n//10
if a1>0:
    cnt=1
    a1=a1-1
else:
    if a2>0:
        cnt=2
        a2=a2-1
    else:
        if a3>0:
            cnt=3
            a3=a3-1
        else:
            if a4>0:
                cnt=4
                a4=a4-1
            else:
                if a5>0:
                    cnt=5
                    a5=a5-1
                else:
                    if a6>0:
                        cnt=6
                        a6=a6-1
                    else:
                        if a7>0:
                            cnt=7
                            a7=a7-1
                        else:
                            if a8>0:
                                cnt=8
                                a8=a8-1
                            else:
                                if a9>0:
                                    cnt=9
                                    a9=a9-1
while a0>0:
    cnt=cnt*10
    a0=a0-1
while a1>0:
    cnt=cnt*10+1
    a1=a1-1
while a2>0:
    cnt=cnt*10+2
    a2=a2-1
while a3>0:
    cnt=cnt*10+3
    a3=a3-1
while a4>0:
    cnt=cnt*10+4
    a4=a4-1
while a5>0:
    cnt=cnt*10+5
    a5=a5-1
while a6>0:
    cnt=cnt*10+6
    a6=a6-1
while a7>0:
    cnt=cnt*10+7
    a7=a7-1
while a8>0:
    cnt=cnt*10+8
    a8=a8-1
while a9>0:
    cnt=cnt*10+9
    a9=a9-1
print (cnt)