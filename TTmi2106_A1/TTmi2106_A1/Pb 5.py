k=int(input())
ok=0
cnt=1
while ok==0:
    if((cnt*(cnt+1))/2>=k):
        ok=1
        print (cnt)
    else:
        cnt+=1
'''we use the Gauss sum to determine the integer located at the index k 
because every number repeats itself by its value, ex 1 is 1 time 2 is 2
times 3 is 3 times etc. and togheter they make the sum'''