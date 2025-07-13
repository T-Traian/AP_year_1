def nr(x):
    cnt=0
    while x>0:
        if x%10==5:                     #function to determine how many digits of 5 there are in a number
            cnt+=1
        x=x//10
    return cnt

k=0
x=int(input())
y=int(input())
if x!=0 and y!=0:                       #we read both x and y at the start and we continue to read y until it reaches 0
    while y!=0:                         #and x takes the last value of y to ensure consecutivety
        if nr(x)>nr(y):
            k+=1
        x=y
        y=int(input())
else:
    print(0)
print (k)