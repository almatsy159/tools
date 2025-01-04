date='1/2/21'
day=""
mon=""
year=""
x=0
for i in range(len(date)):
    if date[i] =="/":
        if i <2:
            day=date[x:i]
            x=i+1
        elif i<4:
            mon=date[x:i]
            year=date[i+1:]

print("day :",day,"; month :",mon,"; year :",year)

if len(day)==1:
    day="0"+str(day)
if len(mon)==1:
    mon="0"+str(mon)
if len(year) ==2:
    year = "20"+str(year)


print("day :",day,"; month :",mon,"; year :",year)    
