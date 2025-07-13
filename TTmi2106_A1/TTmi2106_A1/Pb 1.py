#problem 1
year=int(input())
while year>9:
    cnt=0
    while year>0:
        cnt+=year%10
        year=year//10
    year=cnt
print (int(year))
'''We use 2 whiles to determine the control digit of the given number'''