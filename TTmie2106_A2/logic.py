
v=[]
undo_list=[]

def add_array(v,x):
    v.append(x)

def insert_array(v,k,x):
    v.insert(k,x)

def remove_array(v,x):
    v.pop(x)

def remove_array_index(v,a,b):
    if a>b:
        a,b=b,a     #we switch in case a>b so that we have an interval
    while a<=b:
        v.pop(a)    #we remove every element from [a,b]
        b-=1

def replace_array(v,x,y):
    for i in range(len(v)):
        if v[i]==x:
            v[i]=y      #we replace every x with y

def prime(x):
    if x<2:
        return 0
    else:
        if x==2:                        #prime function, if x is even it is automatically not prime
            return 1                    #we check in for only odd numebers from 3 to x/2+1
        else:
            if x%2==0:
                return 0
            else:
                for i in range(3,x//2+1,2):
                    if x%i==0:
                        return 0
    return 1
def prime_array(v,x,y):
    if x>y:
        x,y=y,x
    while x<=y:
        if prime(v[x])==0:
            v.pop(x)
            y-=1
        else:
            x+=1
    return v

def odd_array(v,x,y):
    if x>y:
        x,y=y,x
    while x<=y:
        if v[x]%2==0:
            v.pop(x)
            y-=1
        else:
            x+=1
    return v

def sum_array(v,x,y):
    s=0
    if x>y:
        x,y=y,x
    while x<=y:
        s+=v[x]         #the sum of the elements from [x,y]
        x+=1
    return s


def gcd(a, b):
    if b == 0:
        return a  # determines the gcd of 2 numbers
    else:
        return gcd(b, a % b)
def gcd_array(v, x, y):
    if len(v) == 1:
        return v[0]
        exit()
    if x > y:
        x, y = y, x
    a = gcd(v[0], v[1])  # we use the gcd of the first 2 values in the list
    x += 2  # then that number goes back in the gcd function with the third number and so on
    while x < y:
        a = gcd(a, v[x])
        x += 1
    return a

def max_array(v,x,y):
    if x>y:
        x,y=y,x
    a=v[0]
    while x<y:
        a=max(a,v[x+1])
        x+=1
    return a

def filter_prime(v):
    cnt=0
    while cnt<len(v):
        if prime(v[cnt])!=1:    #if its prime we remove it
            v.pop(cnt)
            cnt-=1  #very important cnt-=1 so that we check the number left behind from pop
        cnt+=1

def filter_negative(v):
    cnt=0
    while cnt<len(v):
        if v[cnt]>0:
            v.pop(cnt)
            cnt-=1
        cnt+=1

def undo(undo_list,v):
    if len(undo_list)>0:
        v[:]=undo_list.pop()
        print(v)
    else:
        print("No actions to undo.")

