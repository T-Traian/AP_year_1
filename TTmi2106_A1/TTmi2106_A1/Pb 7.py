n=int(input())
v=[1]
k=0
while k<n:
    x=v[k]
    k+=1
    v.append(2*x+1)
    v.append(3*x+1)
v=sorted(set(v))            #we sort the list and get rid of any duplicates
print(v[:k])                #in the list we have more then n numbers but we print only the first k