d=int(input())
m=int(input())
y=int(input())
cd=28
cm=9
cy=2009
k=0
if cy%4==0 and cy%10!=0:
    v = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    v = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
k+=v[m]-d+1
m+=1
while m<cm:
    k+=v[m]
    m+=1
k=k+cd
print (k)