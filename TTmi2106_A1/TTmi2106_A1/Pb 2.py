y=int(input())
d=int(input())
if y%4==0 and y%100!=0:
    v=[0,31,29,31,30,31,30,31,31,30,31,30,31]                       #list of days for leap year
    cnt=1
    while d>29:
        d-=v[cnt]
        cnt+=1
else:
    v = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]         #list of days for normal year
    cnt = 1
    while d > 29:
        d -= v[cnt]
        cnt += 1
if cnt<10:
    print (d,'.','0',cnt,'.',y,sep='')
else:
    print(d,'.',cnt,'.',y,sep='')
