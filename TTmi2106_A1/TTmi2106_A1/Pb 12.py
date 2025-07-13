x=int(input())
y=int(input())
v=[0]*10
a=[0]*10
cnt=0
while x>0:
    v[x%10]=1
    x=x//10
while y>0:                  #we use 2 lists which contain 1 or 0 for each possible number from 0 to 9
    a[y%10]=1               #we compare the 2 lists and if we find that one has an element and the other does not we say "No"
    y=y//10
for i in range (0,10):
    if v[i]!=a[i]:
        print ("No")
        exit()
print ("Yes")