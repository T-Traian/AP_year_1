day=int(input())
month=int(input())
year=int(input())
cday=4
cmonth=3
cyear=2002
cnt=cyear-year
if month>cmonth:
    cnt-=1
else:
    if month==cmonth:
        if day>cday:
            cnt-=1
print (cnt)