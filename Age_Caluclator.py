born_date=int(input("Enter birthday date (DD):"))
born_mnt=int(input("enter birthday month(MM):"))
born_year=int(input("enter birthday year(YY):"))
present_date=int(input("Enter present  date (DD):"))
present_mnt=int(input("enter  present month(MM):"))
present_year=int(input("enter present  year(YY):"))
days=0
if born_year<present_year:
    for i in range(present_year-born_year):
        yu=born_year+i
        if yu%4==0 or yu%100==0:
            days+=366
        else:
            days+=365
def mnt(num1,year):
    td=0
    for n in range(1,num1+1):
        if n==2 or n==4 or n==6 or n==8 or n==9 or n==11:
            td+=31
        elif n==5 or n==7 or n==12 or n==10:
            td+=30
        elif n==3:
            if year%4==0 or n%100==0:
                td+=29
            else:
                td+=28
    return td
day=mnt(present_mnt,present_year)-mnt(born_mnt,born_year)+present_date-born_date
if day<=0:
    t=present_year-born_year-1
    print("Years:",t)
    print("Days:",365-abs(day))
else:
    print("Years:",present_year-born_year)
    print("Days:",abs(day))
days+=day
print(days,"Days")
print(days*86400,"seconds")
