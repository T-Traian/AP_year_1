def sum(x):
    s=0
    while x>0:                  #this function determinates the sum of the digits of a number
        s+=x%10
        x=x//10
    return s
n=int(input())
x=n-1
while x>0:                      #we find the m by going from the initial n to 0
    if (x+sum(x))==n:
        print("Yes")
        exit()
    x-=1
print("No")